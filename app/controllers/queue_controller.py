import json
import time
import zmq
from flask import jsonify

from app import app

import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.RCVTIMEO = 1000
@app.route("/queue/<company_symbol>",methods=["POST"])
def push_message(company_symbol):
    socket.send_string(company_symbol)

    message = socket.recv()

    return jsonify(json.loads(message.decode("utf-8")))