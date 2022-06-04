from Enums import OrderType, Size, CrustType
from HelperFunctions import moneyString
from MenuItem import MenuItem, PizzaMenuItem, ToppingMenuItem
from OrderFactory import OrderFactory
from OrderFoodItems import OrderFoodInfo, OrderItem, PizzaOrderItem

def main():
    #Fake menu items that would be in database
    menuItem1 = MenuItem(1, "Garlic Knots", 6.99, 'Garlicy Bread')
    menuItem2 = MenuItem(2, "Cinnamon Twists", 7.99, 'Made with CinnaMagic')
    pizza1 = PizzaMenuItem(3, 5.99, Size.SMALL, CrustType.HAND_TOSSED)
    pizza2 = PizzaMenuItem(4, 8.99, Size.MEDIUM, CrustType.PAN)
    topping1 = ToppingMenuItem(5, 'Pepperoni', 'Small red meat circles', [1, 1.25, 1.75, 2])
    topping2 = ToppingMenuItem(5, 'Premium Chicken', 'Fancy Chicken', [1.5, 2, 2.25, 2.5])

    item1 = OrderItem(menuItem1, 1)
    item2 = OrderItem(menuItem2, 3)
    item3 = PizzaOrderItem(pizza1, 1)
    item4 = PizzaOrderItem(pizza2, 2)
    item4.addTopping(topping1)
    item4.addTopping(topping2)

    order = OrderFoodInfo()
    order.add(item1)
    order.add(item2)
    order.add(item3)
    order.add(item4)

    print("Showing iterator design pattern")
    print('Useful for customers to look through their order')
    iterator = order.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)

    print('Cost of order: ' + moneyString(order.getTotalCost()))
    print()
    print('Remove Last Item')
    iterator.remove()
    print('New Last Item: ')
    print(iterator.curr())
    print('New Cost: ' + moneyString(order.getTotalCost()))

    print()
    print()
    print('Showing prototype design pattern')
    print('Useful for customer to base new orders off of previous orders')
    print('Creating order 2 as copy of order 1')
    order2 = order.clone()
    iterator = order2.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)
    print('Removing last item')
    iterator.remove()
    iterator = order2.iterator()
    print('Order 1 cost: ' + moneyString(order.getTotalCost()))
    print('Order 2 cost: ' + moneyString(order2.getTotalCost()))
    if(order2.getTotalCost() != order.getTotalCost()):
        print('Changing order 2 did not affect the previous order, items successfuly cloned')
    else:
        print('Orders not successfully cloned')    

    print()
    print()
    print('Showing abstract factory design pattern')
    print('Used to create different types of orders')
    print('Creating Carryout')
    carryout = OrderFactory.create(OrderType.CARRYOUT, 'John', 'Doe', order2)
    print(carryout.getConfirmationMessage())
    print(carryout) 
    print()

    print('Creating Carside')
    carside = OrderFactory.create(OrderType.CARSIDE, "Jane", "Doe", order2, "Honda", "Blue")
    print(carside.getConfirmationMessage())
    print(carside) 
    print()
    
    print('Creating Delivery')
    delivery = OrderFactory.create(OrderType.DELIVERY, "John", "Smith", order, "123 tree Rd")
    print(delivery.getConfirmationMessage())
    print(delivery) 


main()