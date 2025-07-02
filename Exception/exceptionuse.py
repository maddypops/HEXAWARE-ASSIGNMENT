from Exception.InsufficientStockException import InsufficientStockException
from Exception.PaymentFailedException import PaymentFailedException
from .InvalidDataException import InvalidDataException

import randomgit
def process_order(order_detail):
    if order_detail.quantity > order_detail.product.stock:
        raise InsufficientStockException("Not enough stock for this product.")
    else:
        order_detail.product.update_stock(order_detail.quantity)
        print(f"Order processed for {order_detail.product.name}")


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.price = price  # uses setter
        self.stock = stock  # uses setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise InvalidDataException("Product price cannot be negative.")
        self.__price = value




def process_payment():
    if random.choice([True, False]):
        raise PaymentFailedException("Payment was declined.")
    else:
        print("Payment successful.")


try:
    with open("logfile.txt", "a") as log:
        log.write("Order processed successfully\n")
except IOError:
    print("Logging failed.")
