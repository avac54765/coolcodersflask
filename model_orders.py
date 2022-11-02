import random

orders_list = [
    "Sam Smith",

]



    

# adding an order from frontend
def addOrder(order):
    orders_list.append(order)

# Return all items from orders_data
def getOrders():
    return(orders_list)


# Pretty Print item
def printOrder(order):
    print("Customer Name", order['customer-name'], "\n", "Item Purchased:", order['item'], "\n", "Quantity:", order['quantity'], "\n")

# Number of items
def countOrders():
    return len(orders_list)






# Test Stock Model
if __name__ == "__main__": 

    # adding an order for the test
    addOrder({"customer-name":"Sam Smith", "item":"hoodie", "quantity":2})  
    
    # Count of orders
    print("Orders Count: " + str(countOrders()))

    print("Orders List: " + str(getOrders()))
    
