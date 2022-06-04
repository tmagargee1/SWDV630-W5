from Enums import Size
from HelperFunctions import moneyString

class MenuItem:
    def __init__(self, id, name, price, description):
        self.id = id #Would be assigned automatically in future
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        return "{}: {} : {}".format(self.name, moneyString(self.price), self.description)


class PizzaMenuItem(MenuItem):
    def __init__(self, id, price, size, crustType):
        name = '{} Pizza'.format(size)
        description = 'Cheese pizza with {} crust'.format(crustType)

        super().__init__(id, name, price, description)
        self.size = size
        self.crustType = crustType


class ToppingMenuItem(MenuItem):
    def __init__(self, id, name, description, priceArray):
        super().__init__(id, name, priceArray[0], description)
        self.priceArray = priceArray #Array of prices based on size

    def updatePrice(self, size):
        self.price = self.priceArray[size.value]

