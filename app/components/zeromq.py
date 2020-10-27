import json
import time
import zmq

from app.components.yahooApi import YahooApi

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    #  Wait for next request from client
    print("CONNECTED")
    message = socket.recv()
    print("Received request: %s" % message)
    message = message.decode("UTF-8")
    #  Do some 'work'
    try:
        response = YahooApi((message)).get_price()
    except Exception as e:
        socket.send_json({"has_error":True,"message":str(e)})
    finally:
        socket.send_json({"has_error": False, "price": float(response)})
