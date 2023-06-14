from flask import Flask, render_template, request
from main import get_candlestick_data, save_to_csv, get_market_caps

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


app = Flask(__name__)

SYMBOLS = [
    "ADAUSDT",
    "DOGEUSDT",
    "TRXUSDT",
    "MATICUSDT",
    "SOLUSDT",
    "LTCUSDT",
    "DOTUSDT",
    "BUSDDAI",
    "AVAXUSDT",
    "SHIBUSDT",
]


@app.route("/candlestick")
def candlestick():
    symbol = request.args.get("symbol", default="BTCUSDT")
    interval = request.args.get("interval", default="1m")

    candlestick_data = get_candlestick_data(symbol, interval)
    save_to_csv(candlestick_data, symbol, interval)

    df = pd.read_csv(f"{symbol}-{interval}.csv")

    candlestick_df = go.Figure(
        data=[
            go.Candlestick(
                x=df["Open time"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
            )
        ]
    )
    candlestick_json = candlestick_df.to_json()

    return render_template(
        "candlestick.html",
        candlestick=candlestick_json,
        symbol=symbol,
        interval=interval,
    )


@app.route("/piechart")
def piechart():
    market_caps = get_market_caps(SYMBOLS)
    df_market_caps = pd.DataFrame(
        {"Symbol": SYMBOLS, "Market Cap": market_caps}
    )

    pie = px.pie(df_market_caps, values="Market Cap", names="Symbol")
    pie_json = pie.to_json()

    return render_template("piechart.html", pie=pie_json)


if __name__ == "__main__":
    app.run()
