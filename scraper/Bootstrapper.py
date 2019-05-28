from services.BookScraper import BookScraper

if __name__ == '__main__':
    #INFO: servicio scraper, este servicio solamente lee y guarda la información en formato .JSON
    scraper = BookScraper("http://books.toscrape.com")
    scraper.run()
    #TODO: servicio para guardar datos