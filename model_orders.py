import random

orders_list = {
    "Sam":{"item":"hoodie", "Quantity":2}
}

print(orders_list["Sam"]["Quantity"])


    

# adding an order from frontend
def addOrder(customer, item, quantity):
    if customer not in orders_list.keys():
        orders_list[customer] = {"item":item,"Quantity":quantity}
    return {customer:{"item":item, "Quantity":quantity}}

# Return all items from orders_data
def getOrders():
    return(orders_list)


# Pretty Print item
def printOrder(order):
    print("Customer Name", order['customer-name'], "\n", "Item Purchased:", order['item'], "\n", "Quantity:", order['quantity'], "\n")

# Number of items
def countOrders():
    return len(orders_list)

addOrder("jerry", "shirt", 3)






# Test Stock Model
if __name__ == "__main__": 

    # adding an order for the test
    addOrder({"customer-name":"Sam Smith", "item":"hoodie", "quantity":2})  
    
    # Count of orders
    print("Orders Count: " + str(countOrders()))

    print("Orders List: " + str(getOrders()))
    
