from flask import Flask, render_template, request
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import os

# Set up Flask app
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

def get_stock_data(ticker):
    """Fetch stock data from Yahoo Finance."""
    print(f"Fetching data for {ticker}...")
    try:
        stock = yf.download(ticker, start="2023-01-01", end="2024-12-31")
        if stock.empty:
            print(f"Error: No data found for {ticker}")
            return None
        stock = stock.fillna(method='ffill')  # Fill missing values
        print(f"Data fetched: {len(stock)} rows")
        return stock
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def create_price_plot(stock_data, ticker):
    """Generate and return a closing price plot."""
    print(f"Creating price plot for {ticker}...")

    if stock_data is None or stock_data.empty:
        print("Error: Cannot generate plot due to missing data.")
        return None

    plt.figure(figsize=(10, 6))

    try:
        plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
        plt.title(f'{ticker} Closing Prices')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save plot to bytes
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()

        return plot_url

    except Exception as e:
        print(f"Error in create_price_plot: {e}")
        plt.close()
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page to input ticker and display stock closing price plot."""
    plot_url = None
    ticker = ""

    if request.method == 'POST':
        ticker = request.form['ticker'].upper()

        try:
            print(f"Processing request for {ticker}...")
            stock_data = get_stock_data(ticker)

            if stock_data is not None:
                plot_url = create_price_plot(stock_data, ticker)
                print("Plot created successfully.")
            else:
                print("No data received for ticker.")
        except Exception as e:
            print(f"Error occurred: {e}")
            plot_url = None

    return render_template('index.html', plot_url=plot_url, ticker=ticker)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
