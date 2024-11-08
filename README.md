# Crypto Price Bot

This is a Telegram bot that retrieves real-time prices for selected cryptocurrencies (BTC, ETH, and PAXG) in both USD and USDT from the Binance API. The bot sends these prices to a specified Telegram channel every 5 minutes, comparing them with the previous day’s prices and showing trends with appropriate emojis.

## Features

- Fetches real-time prices for Bitcoin (BTC), Ethereum (ETH), and PAX Gold (PAXG) in both USD and USDT.
- Updates prices every 5 minutes.
- Compares current prices with previous day’s values to show a trend (increased/decreased) with emojis.
- Sends formatted messages directly to a specified Telegram channel.

## Project Structure

```plaintext
Crypto-Price-Bot/
├── config/
│   └── config.py           # Contains API key and channel ID for security purposes
├── src/
│   ├── main.py             # Main script for executing the bot
│   ├── price_checker.py    # Module to fetch cryptocurrency prices from Binance API
│   └── utils.py            # Helper functions for formatting messages and managing data
│
└── requirements.txt        # Python dependencies
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Crypto-Price-Bot.git
   cd Crypto-Price-Bot
   ```

2. **Install Dependencies:**

   Make sure you have Python 3 installed, then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Configuration:**

   In the `config/` folder, create a `config.py` file and add the following:

   ```python
   TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
   TELEGRAM_CHANNEL_ID = '@your_channel_id'
   ```

   Replace `your_telegram_bot_token` with your Telegram bot token and `@your_channel_id` with your channel’s ID.

4. **Run the Bot:**

   Execute the bot using:

   ```bash
   python src/main.py
   ```

## Usage

Once the bot is running, it will send updates to your Telegram channel every 5 minutes, showing the real-time prices of BTC, ETH, and PAXG in both USD and USDT. It will also display emojis indicating price trends (up or down) compared to the previous day's values.

## Customization

- **Change Cryptocurrency Symbols:**  
  You can modify the symbols in `src/price_checker.py` if you want to monitor different cryptocurrencies.

- **Modify Update Interval:**  
  In `src/main.py`, adjust the interval in seconds to change how frequently the bot updates prices.

## Security

Ensure you keep your bot token and channel ID secure. Avoid pushing `config.py` directly to public repositories. Instead, use environment variables or add `config.py` to your `.gitignore` file.

## Dependencies

See `requirements.txt` for a full list of required packages. Key dependencies:

- `python-telegram-bot` - For interacting with Telegram’s API.
- `requests` - For making HTTP requests to the Binance API.


## Contributing

Feel free to submit issues, create pull requests, or suggest improvements. 

## Contact

For any questions or support, please contact mahdimoghassemi@gmail.com.
---

