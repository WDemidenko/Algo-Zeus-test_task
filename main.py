from datetime import datetime

import requests
import csv

from flask import abort


def get_candlestick_data(symbol, interval):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"

    response = requests.get(url)
    if response.status_code == 200:
        klines = response.json()
        return klines
    else:
        abort(400, "Provided symbol is not correct")


def save_to_csv(data, symbol, interval):

    filename = f"{symbol}-{interval}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Open time",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Close time",
            "Quote asset volume",
            "Number of trades",
            "Taker buy base asset volume",
            "Taker buy quote asset volume"
        ])
        for row in data:
            open_time = datetime.fromtimestamp(int(row[0]) / 1000)
            close_time = datetime.fromtimestamp(int(row[6]) / 1000)
            row[0] = open_time.strftime('%Y-%m-%d %H:%M:%S')
            row[6] = close_time.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(row[:11])


def get_market_caps(symbols):

    url = "https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products"
    response = requests.get(url)
    data = response.json()

    market_caps = []
    for symbol in symbols:
        for item in data["data"]:
            if item["s"] == symbol:
                circulating_supply = item["cs"]
                current_price = float(item["c"])
                market_cap = circulating_supply * current_price
                market_caps.append(market_cap)
                break

    return market_caps
