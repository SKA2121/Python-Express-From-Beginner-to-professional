# Define the products' classs
class Product:
    def __init__(self, name, Quantity, price):
        self.name = name
        self.Quantity = Quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        for product in self.products:
            print(f"Name : {product.name}, Quantity : {product.Quantity}, price : {product.price}")

    def total_value_inventory(self):
        total = sum(product.Quantity * product.price for product in self.products)
        return total

# Using the Inventory class
inventory = Inventory()
product1 = Product("Book", 10, 15)
product2 = Product("Pen", 100, 1)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.display_inventory()

total_value = inventory.total_value_inventory()
print(f"total in inventory : {total_value} €")
