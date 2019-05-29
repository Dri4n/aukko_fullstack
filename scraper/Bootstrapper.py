from services.BookScraper import BookScraper
from services.BookParser import BookParser

if __name__ == '__main__':
    #INFO: este servicio se encarga de leer y guardar la información en formato .JSON
    scraper = BookScraper("http://books.toscrape.com")
    scraper.run()
    #TODO: servicio para guardar datos
    parser = BookParser()
    parser.run()
