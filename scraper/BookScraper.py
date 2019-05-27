import requests
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


class BookScrapper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.pool = ThreadPoolExecutor(max_workers=20)

        self.readed_pages = set([])
        self.readed_books = set([])

        self.crawl_pages_queue = Queue()
        self.crawl_books_queue = Queue()

        self.read_pages(self.base_url)

    def read_pages(self, page_url):
        next_page = page_url
        while next_page:
            response = self.scrape(next_page)
            soup = BeautifulSoup(response.text, 'html.parser')
            next_link = soup.select('li.next a[href]')
            if len(next_link):
                next_page = self.link_to_absolute_path(next_link[0]['href'])
                page_books = soup.select('article.product_pod > h3 > a[href]')
                if (len(page_books)):
                    for page_book in page_books:
                        page_book_url = page_book['href']
                        print('ADDING BOOK TO QUEUE: {}'.format(page_book_url))
                        self.crawl_books_queue.put(self.link_to_absolute_path(page_book_url))
            else:
                break

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
        price = product_main.find('p', { 'class': 'price_color' }).get_text()
        thumbail = self.link_to_absolute_path(soup.find('div', { 'id' : 'product_gallery' }).find('img').get('src'))

        print('BOOK {} PRICE {} - IMAGE_URL = {}'.format(title, price, thumbail))

    def scrape_info(self, html):
        return

    def scrape_book_response(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.read_book_info(result.text)

    def scrape(self, url):
        res = requests.get(url)
        return res

    def run(self):
        while True:
            try:
                book_url = self.crawl_books_queue.get(timeout=60)
                if book_url not in self.readed_books:
                    self.readed_books.add(book_url)
                    job = self.pool.submit(self.scrape, book_url)
                    job.add_done_callback(self.scrape_book_response)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue

if __name__ == '__main__':
    scraper = BookScrapper("http://books.toscrape.com")
    scraper.run()