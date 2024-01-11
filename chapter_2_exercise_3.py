from abc import ABC, abstractmethod

class InstrumentMusical(ABC):
    def __init__(self, name, price_rent):
        self.name = name
        self.price_rent = price_rent

    @abstractmethod
    def description(self):
        pass

class Guitar(InstrumentMusical):
    def __init__(self, name, price_rent, type_guitar):
        super().__init__(name, price_rent)
        self.type_guitar = type_guitar

    def description(self):
        return f"Guitar {self.name} ({self.type_guitar}), Price of Renting : {self.price_rent} € monthly"

class Piano(InstrumentMusical):
    def __init__(self, name, price_rent, brand):
        super().__init__(name, price_rent)
        self.brand = brand

    def description(self):
        return f"Piano {self.name} ({self.brand}), Price of Renting : {self.price_rent} € monthly"

class battery(InstrumentMusical):
    def __init__(self, name, price_rent, model):
        super().__init__(name, price_rent)
        self.model = model

    def description(self):
        return f"Battery {self.name} ({self.model}), Price of Renting : {self.price_rent} € monthly"

# Using the classes
Guitar = Guitar("Acoustique", 30, "Classique")
piano = Piano("A queue", 50, "Yamaha")
battery = battery("Electronic", 40, "Roland")

instruments = [Guitar, piano, battery]

for instrument in instruments:
    print(instrument.description())
