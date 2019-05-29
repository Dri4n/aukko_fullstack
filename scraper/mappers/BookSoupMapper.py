import re
from utils import GetPreviousSibling, GetNextSibling

#INFO: clase destinada a mapear los datos del libro a partir de una instancia de BeautifulSoup (soup)
class BookSoupMapper:
    def __init__(self, soup):
        self.set_sections(soup)
        self.set_elements(soup)
        self.set_elements_values()
    
    def set_sections(self, soup):
        self.navegation_section = soup.find('ul', { 'class' : 'breadcrumb' })
        self.main_section = soup.find('div', { 'class' : 'product_main' })
        self.description_section = soup.find('div', { 'id' : 'product_description' })
        self.information_section = soup.find('table', { 'class' : 'table table-striped' })
        self.thumbail_section = soup.find('div', { 'id' : 'product_gallery' })
        
    def set_elements(self, soup):
        self.title_element = self.main_section.find('h1')
        self.category_element = GetPreviousSibling(self.navegation_section.find('li', { 'class': 'active' }))
        self.thumbail_element = self.thumbail_section.img
        self.description_element = GetNextSibling(self.description_section)
        self.stock_element = self.main_section.find('p', { 'class': 'availability' })
    
    def set_elements_values(self):
        self.read_title()
        self.read_thumbail()
        self.read_category()
        self.read_description()
        self.read_stock()
        self.read_information()

    def read_title(self):
        title = None
        if self.title_element is not None:
            title = self.title_element.get_text()
        self.title = title
    
    def read_thumbail(self):
        thumbail = None
        if self.thumbail_element is not None:
            thumbail = self.thumbail_element.attrs['src']
        self.thumbail = thumbail

    def read_category(self):
        category = None
        category_url = None
        if self.category_element is not None:
            category = self.category_element.a.get_text()
            category_url = self.category_element.a.attrs['href']
        self.category = category
        self.category_url = category_url
    
    def read_description(self):
        description = None
        if self.description_element is not None:
            description = self.description_element.get_text()
        self.description = description

    def read_stock(self):
        in_stock = False
        if self.stock_element is not None:
            stock_element_class = self.stock_element.get('class') or []
            if 'instock' in stock_element_class:
                in_stock = True
        self.stock = in_stock
    
    def read_information(self):
        price = None
        price_tax = None
        upc = None
        tax = None

        rows = self.information_section.findAll('tr')
        if rows is not None and len(rows) > 0:
            for row in rows:
                key = row.find('th').get_text()
                value = row.find('td').get_text()
            
                if key == 'Price (excl. tax)':
                    price = value
                if key == 'Price (incl. tax)':
                    price_tax = value
                if key == 'Tax':
                    tax = value
                if key == 'UPC':
                    upc = value

        self.price = price
        self.price_tax = price_tax
        self.tax = tax
        self.upc = upc
    