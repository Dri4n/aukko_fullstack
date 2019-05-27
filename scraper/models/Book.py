from models.Product import Product

# definción de libro, hereda desde producto.
class Book(Product):
    def __init__(self, title, category, thumbail, price, stock, description, upc):
        Product.__init__(self, title, category, price, description)
        self.thumbail = thumbail
        self.stock = stock
        self.upc = upc
    
    def toString(self):
        print('BOOK {} {}'.format(self.title, self.price))