class Product :
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.ratings = ratings
        self.deal_price = deal_price
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Ratings : {}".format(self.ratings))
        print("Deal_price : {}".format(self.deal_price))
        print("You_save : {}".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price


class Electronic_Product(Product) :
    def __init__(self, name, price, deal_price, ratings , warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    def display_product_details(self):
        super().display_product_details()
        print("Warranty : {}".format(self.warranty_in_months))

class Grocery_Item(Product) :
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date


    def display_product_details(self):
        super().display_product_details()
        print("Expiry date : {}".format(self.expiry_date))

class Order :
    def __init__(self,delivery_speed, address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.address = address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart :
            product.display_product_details()
            print("Quantity : {}".format(quantity))
            print(" ")

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print(total_bill)


tv = Electronic_Product("TV", 30000,25000,4, "5 months")
phone = Electronic_Product("Phone",100000, 80000, 8, "6 months")
milk = Grocery_Item("Milk", 30 , 25, 4, "2024")




o = Order("prime" , "hyd")
o.add_item(tv, 1)
o.add_item(milk, 5)
o.display_order_details()
o.get_total_bill()




