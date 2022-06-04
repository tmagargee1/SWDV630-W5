from Enums import OrderType
from OrderFactory import OrderFactory


def main():
    print (OrderFactory.create(OrderType.CARRYOUT, 'John', 'Doe', 'djamkdfnbkjds')) 
    delivery = OrderFactory.create(OrderType.DELIVERY,"John", "Doe", "dfkansmdf", "123 tree Rd")
    print(delivery)

main()