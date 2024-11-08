def format_message(prices):
    message = f"""
    قیمت تتری:

    🪙 BTC (USDT): {prices['BTC_USDT']} {prices['BTC_USDT_change']}

    🟦 ETH (USDT): {prices['ETH_USDT']} {prices['ETH_USDT_change']}

    🔶 PAXG (USDT): {prices['PAXG_USDT']} {prices['PAXG_USDT_change']}
    """
    return message