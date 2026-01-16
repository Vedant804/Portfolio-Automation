import yfinance as yf
from database import get_portfolio_db
from datetime import datetime

def track_my_holdings():
    db = get_portfolio_db()
    if db is None:
      print("❌ Could not connect to the database. Check your .env file.")
      return

    # 1. Define your real assets
    # VEDL.NS = Vedanta, SILVERBEES.NS = Nippon Silver ETF
    assets = ["VEDL.NS", "SILVERBEES.NS","GOLDBEES.NS", "RELIANCE.NS","HDFCBANK.NS","SBIN.NS"]
    
    print(f"--- Market Check at {datetime.now().strftime('%H:%M:%S')} ---")

    for ticker in assets:
        # 2. Fetch live data from Yahoo Finance
        data = yf.Ticker(ticker)
        current_price = round(data.history(period='1d')['Close'].iloc[-1], 2)
        
        # 3. Create a professional log for your database
        log_entry = {
            "ticker": ticker,
            "price": current_price,
            "timestamp": datetime.now(),
            "status": "Automatic_Monitor"
        }
        
        # 4. Save to Cloud (Collection: 'market_logs')
        db.market_logs.insert_one(log_entry)
        print(f"✅ {ticker}: ₹{current_price} (Saved to Cloud)")

if __name__ == "__main__":
    track_my_holdings()