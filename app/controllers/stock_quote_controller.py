import json
import time
import traceback

import zmq
from flask import render_template, jsonify

from app import app, socket
from app.components.yahooApi import YahooApi


@app.route("/api/stock/<symbol>/details", methods=["GET"])
def get_stock_details(symbol):
    """Hello World Route

    This docstring will show up as the description and short-description
    for the openapi docs for this route.
    """
    socket.send_string(symbol)

    time.sleep(1)
    try:
        message = socket.recv()
        return jsonify(json.loads(message.decode("utf-8")))

    except zmq.ZMQError:
        print("error while receivin message")
    except Exception as e:
        print("excpetion {}".format(e))

    yahoo = YahooApi(symbol)
    return jsonify(yahoo.get_details()[symbol])


@app.route("/stock/<symbol>/quote", methods=["GET"])
def get_stock_quote(symbol):
    try:
        yahoo = YahooApi(symbol)
    except Exception as e:
        return render_template("error.html", code=500, message=e.__str__())

    return render_template("nivel1.html", cotacao=yahoo.get_price(), acao=symbol)
