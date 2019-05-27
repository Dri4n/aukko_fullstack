import requests
import re

from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from models.Book import Book
from models.Category import Category

class BookScraper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.pool = ThreadPoolExecutor(max_workers=10)

        self.readed_pages = set([])
        self.readed_books = set([])

        self.crawl_pages_queue = Queue()
        self.crawl_books_queue = Queue()

    def read_categories(self, page_url):
        response = self.scrape(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = [
            Category(category.get_text().strip(), self.link_to_absolute_path(category.get('href')), 'books') 
            for category
            in soup.find_all("a", href=re.compile("catalogue/category/books"))
            if category is not None
        ]

    # metodo en el cual se enconlan los libros a realizar scraping.
    def read_pages(self, page_url):
        next_page = page_url
        while next_page:
            response = self.scrape(next_page)
            soup = BeautifulSoup(response.text, 'html.parser')
            next_link = soup.select('li.next a[href]')
            if len(next_link):
                next_page = self.link_to_absolute_path(next_link[0]['href'])
                page_books = soup.select('article.product_pod > h3 > a[href]')
                page_books_len = len(page_books)
                if (page_books_len):
                    print('INSERT TO QUEUE {} BOOKS FROM PAGE {}'.format(page_books_len, next_page))
                    for page_book in page_books:
                        page_book_url = page_book['href']
                        # print('BOOK ENQUEUED: {}'.format(page_book_url))
                        self.crawl_books_queue.put(self.link_to_absolute_path(page_book_url))
            else:
                break

    # metodo de ayuda con el cual se convierte una ruta relativa en ruta absoluta.
    def link_to_absolute_path(self, relative_path):
        absolute_path = self.base_url
        if ('catalogue' in relative_path):
            absolute_path = urljoin(absolute_path, relative_path)
        else:
            absolute_path = urljoin(absolute_path + '/catalogue/', relative_path)
        return absolute_path

    def read_book_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        product_main = soup.find('div', { 'class' : 'product_main' })

        title = product_main.find('h1').get_text()
        category = ''
        thumbail = self.link_to_absolute_path(soup.find('div', { 'id' : 'product_gallery' }).find('img').get('src'))
        price = product_main.find('p', { 'class': 'price_color' }).get_text()
        stock = ''
        description = ''
        upc = ''

        book_entity = Book(title, category, thumbail, price, stock, description, upc)
        book_entity.toString()

    def scrape_book_response(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.read_book_info(result.text)

    def scrape(self, url):
        res = requests.get(url)
        return res

    def run(self):
        # proceso de lectura de categorias
        self.read_categories(self.base_url)
        # proceso de lectura de paginas (sitio principal)
        self.read_pages(self.base_url)

        # proceso de carga de libros encolados para lectura
        while True:
            try:
                book_url = self.crawl_books_queue.get(timeout=60)
                if book_url not in self.readed_books:
                    self.readed_books.add(book_url)
                    process = self.pool.submit(self.scrape, book_url)
                    process.add_done_callback(self.scrape_book_response)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue