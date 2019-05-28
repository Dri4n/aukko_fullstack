from models.Product import Product

# definción de libro, hereda desde producto.
class Book(Product):
    def __init__ (
        self, 
        title = None, 
        category = None, 
        category_url = None, 
        thumbail = None, 
        price = None, 
        stock = None, 
        description = None, 
        upc = None
    ):
        Product.__init__(self, title, category, category_url, price, description)
        self.thumbail = thumbail
        self.stock = stock
        self.upc = upc
    
    def toString(self):
        print('BOOK {} {}'.format(self.title, self.price))