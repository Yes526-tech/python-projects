class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self.price = price
        else:
            raise ValueError("you can't entry negative numbers")
        def set_price(self, value):
            pass
        def get_price(self):
            pass
p = Product("iphone 12", 9000)
p.price = -8000
print(p.price)
