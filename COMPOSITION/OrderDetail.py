class OrderDetail:
    def __init__(self, order, product, quantity):
        if product is None:
            raise Exception("Incomplete order: No product selected.")
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity
