class Plate:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.plates = []

    def add_plate(self, plate, quantité=1):
        self.plates.append((plate, quantité))

    def compute_total(self):
        total = sum(plate.price * quantité for plate, quantité in self.plates)
        return total

    def display_facture(self):
        print("Billing Order :")
        for plate, quantité in self.plates:
            print(f"{plate.name} x{quantité} : {plate.price * quantité} €")
        total = self.compute_total()
        print(f"Total : {total} €")

# Using the order class 
order = Order()
pizza = Plate("Pizza", 12.50)
Pasta = Plate("Pasta", 8.75)

order.add_plate(pizza, 2)
order.add_plate(Pasta, 1)

order.display_facture()
