def compare_prices(current_price, price_24h):
    if current_price > price_24h:
        return "🟢" 
    elif current_price < price_24h:
        return "🔴"  
    else:
        return "🟡" 