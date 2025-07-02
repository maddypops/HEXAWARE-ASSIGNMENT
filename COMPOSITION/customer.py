class Customer:
    def __init__(self, customer_id, name, email):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
