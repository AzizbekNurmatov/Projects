from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import datetime
import threading
from flask_caching import Cache

# Flask setup
app = Flask(__name__)

# Caching setup (stores data in memory for 5 minutes)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

cache.init_app(app)

def get_stock_data(ticker, days=30):
    """Fetch stock data for the last `days` days to minimize API calls."""
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.today() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')

    stock = yf.download(ticker, start=start_date, end=end_date)
    
    if stock.empty:
        return None

    return stock.fillna(method='ffill')

@cache.memoize(timeout=300)  # Cache results for 5 minutes
def get_stock_data_cached(ticker, days):
    return get_stock_data(ticker, days)

def fetch_stock_data_async(ticker, days, result_dict):
    """Fetch stock data asynchronously and store it in result_dict."""
    result_dict[ticker] = get_stock_data_cached(ticker, days)

def create_price_plot(stock_data, ticker):
    """Generate and return a closing price plot with a 20-day moving average."""
    if stock_data is None or stock_data.empty:
        return None

    plt.figure(figsize=(10, 6))

    # Plot closing price
    plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')

    # Add 20-day moving average
    stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
    plt.plot(stock_data.index, stock_data['SMA_20'], label='20-Day SMA', color='red', linestyle='--')

    plt.title(f'{ticker} Closing Prices & Moving Avg')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save and encode image
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    ticker = ""
    stock_info = {}
    selected_time = 30  # Default time range

    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        selected_time = int(request.form.get('time_range', 30))  # Convert to integer
        result_dict = {}

        # Fetch data asynchronously
        fetch_thread = threading.Thread(target=fetch_stock_data_async, args=(ticker, selected_time, result_dict))
        fetch_thread.start()
        fetch_thread.join()

        stock_data = result_dict.get(ticker)

        if stock_data is not None:
            plot_url = create_price_plot(stock_data, ticker)

            # Extract latest OHLC data
            latest = stock_data.iloc[-1]
            stock_info = {
                "Open": round(latest["Open"], 2),
                "High": round(latest["High"], 2),
                "Low": round(latest["Low"], 2),
                "Close": round(latest["Close"], 2)
            }

    return render_template('index.html', plot_url=plot_url, ticker=ticker, stock_info=stock_info, selected_time=selected_time)

if __name__ == '__main__':
    app.run(debug=True)
