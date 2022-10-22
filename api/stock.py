from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_stock import *

stock_api = Blueprint('stock_api', __name__,
                   url_prefix='/api/stocks')

api = Api(stock_api)

class stockapi:
    # not implemented
    class _Create(Resource):
        def post(self, item):
            pass

         
    # get getStock
    class _Read(Resource):
        def get(self):
            return jsonify(getStock())

    
    # getStock(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getStock(id))

     # number of different items in stock
    class _ReadCount(Resource):
        def get(self):
            count = countStocks()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: SubtractStockQuantity
    class _UpdateQuantity(Resource):
        def put(self, id):
            SubtractStockQuantity(id)
            return jsonify(getStock(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:stock>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateQuantity, '/quantity/<int:id>')
    
        
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://coolcoders.nighthawkscrums.gq' # run from web
    url = server + "/api/stocks"
    responses = []  # responses list

    # get count of items on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update quantity test sequence
    num = str(random.randint(0, count-1)) # test a random item
    responses.append(
        requests.get(url+"/"+num)  # read item by id
        ) 
    responses.append(
        requests.put(url+"/quanitity/"+num) # quantity to count URL
        ) 
    
    # obtain a random item
    responses.append(
        requests.get(url+"/random")  # list a random item
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")