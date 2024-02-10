class Cart:
    flat_discount = 200
    min_bill = 100
    def __init__(self):
        self.items ={}
        self.price_details = {"book" : 10, "laptop" : 30000}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity
        self.display_products()

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_items(self):
        items_list = []
        items_list = list(self.items.keys())
        print(items_list)

    def total_price(self) :
        total_price = 0
        for item_name, quantity in self.items.items():
            print(item_name, quantity)
            place = self.price_details[item_name]
            print(place)
    def display_products(self):
        print(self.items)
    def get_min_bill(self):
        print(Cart.min_bill)
    @classmethod
    def update_flat_discount(cls, new_discount):
        cls.flat_discount = new_discount

    @classmethod
    def increase_flat_discount(cls, extra_discount):
        new_discount = cls.flat_discount + extra_discount
        cls.update_flat_discount(new_discount)

    @staticmethod
    def greet():
        print("Have a good day")

Cart.greet()
# Cart.increase_flat_discount(300)
# print(Cart.flat_discount)
# cart_obj = Cart()
# a = Cart()
# a.add_item("book", 10)
# a.add_item("laptop",10)
# a.display_products()
# cart_obj.add_item("book",10)
# cart_obj.add_item("laptop",1)
# cart_obj.get_items()
# cart_obj.remove_item("laptop")
# cart_obj.get_items()
# cart_obj.update_quantity("book", "20")
# cart_obj.get_items()
# cart_obj.add_item("laptop", 5)
# cart_obj.get_items()
# cart_obj.total_price()
# cart_obj.display_products()


