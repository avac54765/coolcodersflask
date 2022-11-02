import random

stock_data = []
stock_list = [
    "Nighthawk Headquaters Hoodie",
    "Napping in the Nest Grey Pants",
    "Napping in the Nest PJ Pants",
    "Take Flight Hoodie",
    "Nighthawk North T-Shirt",
]

# Initialize stocks
def initStocks():
    # setup stocks into a dictionary with id, name, description, quantity left of item
    item_id = 1

    for item in stock_list:
        stock_data.append({"id": item_id, "item": item, "quantity": random.randint(1, 100)}) #we chose to randomize the quantity to show purpose of the function
        item_id += 1 #in future, user would need to be able to input a quanitity for each item
    
    

    
# Return all items from stock_data
def getStocks():
    return(stock_data)

# Item getter
def getStock(id):
    return(stock_data[id])

# Pretty Print item
def printStock(stock):
    print(stock['id'], stock['item'], "\n", "quantity:", stock['quantity'], "\n")

# Number of items
def countStocks():
    return len(stock_data)

# Lower quantity by 1
def SubtractStockQuantity(id):
    if stock_data[id]['quantity'] > 0:
        stock_data[id]['quantity'] = stock_data[id]['quantity'] - 1
    return stock_data[id]['quantity']






# Test Stock Model
if __name__ == "__main__": 
    initStocks()  # initialize stocks
    
    # Count of Stocks
    print("Stocks Count: " + str(countStocks()))
    
    