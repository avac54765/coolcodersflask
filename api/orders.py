from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_orders import *  # if testing locally you need to set a python path in your terminal

orders_api = Blueprint('orders_api', __name__,
                   url_prefix='/api/orders')

api = Api(orders_api)

class OrdersApi:
    

    # addOrder
    class _Add(Resource):
     def get(self, customer, item, quantity):
        return jsonify(addOrder(customer, item, quantity))
    

         
    # get getOrders
    class _Read(Resource):
        def get(self):
            return jsonify(getOrders())

    

     # number of different items in orders
    class _ReadCount(Resource):
        def get(self):
            count = countOrders()
            countMsg = {'count': count}
            return jsonify(countMsg)


    # building RESTapi resources/interfaces, these routes are added to Web Server
    # coolcoders.nighthawkcodescrums.gq/api/orders/addorder/sam/hoodie/3
    api.add_resource(_Add, '/addorder/<string:customer>/<string:item>/<int:quantity>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadCount, '/count')
    
        
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://coolcoders.nighthawkcodescrums.gq' # run from web
    url = server + "/api/orders"
    responses = []  # responses list

    # get count of items on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']


    responses.append(
        requests.get(url+"/")  # testing all stock items
        ) 
    
    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")