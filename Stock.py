class Stock:

    def __init__(self, stock_name, products):
        self.stock_name = stock_name
        self.products = products

    def take_from_stock(self, item):
        if item in self.products:
            number_of_items_on_stock = self.products[item]
            self.products[item] = number_of_items_on_stock - 1
            return True

        return False

    def is_in_this_stock(self, item):
        if item in self.products and self.products[item] > 0:
            return True
        return False

    def get_stock_name(self):
        return self.stock_name

    def get_products(self):
        return self.products

    def refill_stock(self):  # update those values only which have become zero
        for key in self.products.keys():
            if self.products[key] == 0:
                self.products[key] = 20
        return self.products
