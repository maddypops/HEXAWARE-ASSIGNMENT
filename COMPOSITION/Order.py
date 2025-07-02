class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer  # Composition
        self.__order_details = []

    @property
    def customer(self):
        return self.__customer

    @property
    def order_details(self):
        return self.__order_details

    def add_order_detail(self, order_detail):
        self.__order_details.append(order_detail)

