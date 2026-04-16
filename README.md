Trading Bot on (BFT) is a modular CLI application built in Python for executing trades on the Binance USDT-M Futures Testnet.
The system supports both Market and Limit orders, along with an integrated risk management layer to control trade.
It enables users to place and manage trades using Binance’s official API in a safe testing environment.



FEATURES

Connect securely to Binance Futures Testnet using your API key & secret
Place Market, Limit, and Stop-Limit orders on supported symbols
Responsive and intuitive Streamlit web interface – no coding required to place orders
Real-time order placement with confirmation and detailed status shown
Input validation and error handling for a smooth user experience
Logs all API requests and responses (logging can be added/enhanced easily)
Easily extensible for advanced order types and integrations

FUTHER ENHANCMENT

RSI / EMA trading strategy engine
Stop-loss & take-profit system
Live price dashboard
Telegram alerts
Paper trading mode


HOW TO RUN
python cli.py place ETHUSDT SELL MARKET 0.01
