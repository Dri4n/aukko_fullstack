from services.BookScraper import BookScraper

if __name__ == '__main__':
    scraper = BookScraper("http://books.toscrape.com")
    scraper.run()