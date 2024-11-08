import time
from src.bot import send_message
from src.price_checker import get_price, get_price_24h
from src.functions import compare_prices
from src.utils import format_message

def main():
    while True:
        btc_usdt_current = get_price('BTCUSDT')
        eth_usdt_current = get_price('ETHUSDT')
        paxg_usdt_current = get_price('PAXGUSDT')
        
        btc_usdt_24h = get_price_24h('BTCUSDT')
        eth_usdt_24h = get_price_24h('ETHUSDT')
        paxg_usdt_24h = get_price_24h('PAXGUSDT')

        btc_usdt_change = compare_prices(btc_usdt_current, btc_usdt_24h)
        eth_usdt_change = compare_prices(eth_usdt_current, eth_usdt_24h)
        paxg_usdt_change = compare_prices(paxg_usdt_current, paxg_usdt_24h)

        prices = {
            'BTC_USDT': btc_usdt_current,
            'ETH_USDT': eth_usdt_current,
            'PAXG_USDT': paxg_usdt_current,
            'BTC_USDT_change': btc_usdt_change,
            'ETH_USDT_change': eth_usdt_change,
            'PAXG_USDT_change': paxg_usdt_change,
        }
        
        message = format_message(prices)

        send_message(message)
        
        time.sleep(10)  

if __name__ == '__main__':
    main()
