from flask import render_template, jsonify

from app import app
from app.components.yahooApi import YahooApi


@app.route("/api/stock/<symbol>/details",methods=["GET"])
def get_stock_details(symbol):
    """Hello World Route

    This docstring will show up as the description and short-description
    for the openapi docs for this route.
    """
    yahoo = YahooApi(symbol)
    return jsonify( yahoo.get_details()[symbol])


@app.route("/stock/<symbol>/quote",methods=["GET"])
def get_stock_quote( symbol):

        try:
            yahoo = YahooApi(symbol)
        except Exception as e:
            return  render_template("error.html", code=500, message=e.__str__())

        return render_template(
            "nivel1.html", cotacao= yahoo.get_price(), acao=symbol
        )