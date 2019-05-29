class Book():
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
        self.title = title
        self.category = category
        self.category_url = category_url
        self.price = price
        self.description = description
        self.thumbail = thumbail
        self.stock = stock
        self.upc = upc
    
    def toString(self):
        print('BOOK {} {}'.format(self.title, self.price))