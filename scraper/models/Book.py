class Book():
    def __init__ (
        self, 
        title, 
        category, 
        category_url, 
        thumbail, 
        price,
        price_tax,
        tax,
        stock, 
        description, 
        upc
    ):
        self.title = title
        self.category = category
        self.category_url = category_url
        self.price = price
        self.price_tax = price_tax
        self.tax = tax
        self.description = description
        self.thumbail = thumbail
        self.stock = stock
        self.upc = upc