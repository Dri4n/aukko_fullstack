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
    
    def set_elements_values(self):
        self.set_title()
        self.set_thumbail()
        self.set_category()
        self.set_description()
        self.set_information()

    def set_title(self):
        title = None
        if (self.title_element is not None):
            title = self.title_element.get_text()
        self.title = title
    
    def set_thumbail(self):
        thumbail = None
        if (self.thumbail_element is not None):
            thumbail = self.thumbail_element.attrs['src']
        self.thumbail = thumbail

    def set_category(self):
        category = None
        category_url = None
        if (self.category_element is not None):
            category = self.category_element.a.get_text()
            category_url = self.category_element.a.attrs['href']
        self.category = category
        self.category_url = category_url
    
    def set_description(self):
        description = None
        if (self.description_element is not None):
            description = self.description_element.get_text()
        self.description = description
    
    def set_information(self):
        self.price = 1000
        self.stock = True
        self.upc = '9528d0948525bf5f'
    