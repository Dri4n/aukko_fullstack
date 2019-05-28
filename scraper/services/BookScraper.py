import requests, re, json, codecs

from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from models.Book import Book
from models.Category import Category
from mappers.BookSoupMapper import BookSoupMapper

class BookScraper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.pool = ThreadPoolExecutor(max_workers=20)

        self.readed_pages = set([])
        self.readed_books = set([])

        self.crawl_pages_queue = Queue()
        self.crawl_books_queue = Queue()

        self.books_data_set = []
        self.categories_data_set = []

    def read_categories(self, page_url):
        response = self.scrape(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = [
            Category(category.get_text().strip(), self.link_to_absolute_path(category.get('href')), 'books') 
            for category
            in soup.find_all("a", href=re.compile("catalogue/category/books"))
            if category is not None
        ]
        self.categories_data_set.extend(categories)

    #INFO: metodo en el cual se enconlan los libros a realizar scraping.
    def read_pages(self, page_url):
        next_page = page_url

        #TODO: solucionar problema de lectura de solo la primera pagina, convertir en metodo recursivo.
        links = 1
        while links > 0:
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
                        self.crawl_books_queue.put(self.link_to_absolute_path(page_book_url))
                links-=1
            else:
                break

    #INFO: metodo de ayuda con el cual se convierte una ruta relativa en ruta absoluta.
    def link_to_absolute_path(self, relative_path):
        absolute_path = self.base_url
        if ('catalogue' in relative_path):
            absolute_path = urljoin(absolute_path, relative_path)
        else:
            absolute_path = urljoin(absolute_path + '/catalogue/', relative_path)
        return absolute_path

    def read_book_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        mapper = BookSoupMapper(soup)
        book_entity = Book(
            mapper.title,
            mapper.category,
            self.link_to_absolute_path(mapper.category_url),
            self.link_to_absolute_path(mapper.thumbail),
            mapper.price, #TODO: leer precio
            mapper.stock, #TODO: leer stock
            mapper.description,
            mapper.upc #TODO: leer upc
        )
        self.books_data_set.append(book_entity)

    def scrape_book_response(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.read_book_info(result.text)

    def scrape(self, url):
        res = requests.get(url)
        return res

    def run(self):
        #INFO: proceso de lectura de categorias
        self.read_categories(self.base_url)
        #INFO: proceso de lectura de paginas (sitio principal)
        self.read_pages(self.base_url)

        #INFO: proceso de carga de libros encolados para lectura
        while True:
            try:
                book_url = self.crawl_books_queue.get(timeout=10)
                if book_url not in self.readed_books:
                    self.readed_books.add(book_url)
                    process = self.pool.submit(self.scrape, book_url)
                    process.add_done_callback(self.scrape_book_response)
            except Empty:
                if (len(self.books_data_set)):
                    json_string = json.dumps([ob.__dict__ for ob in self.books_data_set], ensure_ascii=False)
                    with open('data/books.json', 'w', encoding='utf-8') as f:
                        f.write(json_string)
                if (len(self.categories_data_set)):
                    json_string = json.dumps([ob.__dict__ for ob in self.categories_data_set], ensure_ascii=False)
                    with open('data/categories.json', 'w', encoding='utf-8') as f:
                        f.write(json_string)
                return
            except Exception as e:
                print(e)
                continue