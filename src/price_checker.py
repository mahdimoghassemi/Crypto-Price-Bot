import requests

def get_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def get_price_24h(symbol):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&limit=1'
    response = requests.get(url)
    data = response.json()
    price_24h = float(data[0][1])
    return price_24h