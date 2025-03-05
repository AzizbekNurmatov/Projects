import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Step 1: Download Stock Data
ticker = "AAPL"  # Define the ticker symbol
stock_data = yf.download(ticker, start="2010-01-01", end="2025-01-01")

# Step 2: Preprocess the Data
stock_data['Target'] = stock_data['Close'].shift(-1)
stock_data.dropna(inplace=True)

# Moving Averages
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()

# Price-Based Features
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data['Volatility_10'] = stock_data['Daily_Return'].rolling(window=10).std()
stock_data['Momentum_10'] = stock_data['Close'] / stock_data['Close'].shift(10)

# RSI Calculation
window = 14
delta = stock_data['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
rs = gain / loss
stock_data['RSI'] = 100 - (100 / (1 + rs))

# Exponential Moving Averages
stock_data['12_EMA'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
stock_data['26_EMA'] = stock_data['Close'].ewm(span=26, adjust=False).mean()

# MACD
stock_data['MACD'] = stock_data['12_EMA'] - stock_data['26_EMA']
stock_data['MACD_Signal'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()

# Bollinger Bands
stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
stock_data['20_STD'] = stock_data['Close'].rolling(window=20).std()
stock_data['Upper_Band'] = stock_data['20_MA'] + (stock_data['20_STD'] * 2)
stock_data['Lower_Band'] = stock_data['20_MA'] - (stock_data['20_STD'] * 2)

# Volume-Based Features
stock_data['Volume_Change'] = stock_data['Volume'].pct_change()
stock_data['Volume_MA_10'] = stock_data['Volume'].rolling(window=10).mean()

# Drop NaN values due to rolling calculations
stock_data.dropna(inplace=True)

# Features & Target
features = ['Close', '50_MA', '200_MA', 'Daily_Return', 'Volatility_10',
            'Momentum_10', 'RSI', 'MACD', 'MACD_Signal', 'Upper_Band', 'Lower_Band',
            'Volume_Change', 'Volume_MA_10']
X = stock_data[features]
y = stock_data['Target']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
predictions = model.predict(X_test)

# Evaluate Model
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")

# Plot Features
fig, axes = plt.subplots(4, 2, figsize=(14, 12))
axes = axes.flatten()

# 1. Closing Price & Moving Averages
axes[0].plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
axes[0].plot(stock_data.index, stock_data['50_MA'], label='50-Day MA', color='orange')
axes[0].plot(stock_data.index, stock_data['200_MA'], label='200-Day MA', color='red')
axes[0].set_title('Close Price & Moving Averages')
axes[0].legend()

# 2. Daily Return
axes[1].plot(stock_data.index, stock_data['Daily_Return'], color='purple')
axes[1].set_title('Daily Return')

# 3. Volatility (10-day)
axes[2].plot(stock_data.index, stock_data['Volatility_10'], color='green')
axes[2].set_title('10-Day Volatility')

# 4. RSI
axes[3].plot(stock_data.index, stock_data['RSI'], color='brown')
axes[3].axhline(70, linestyle='--', color='red')
axes[3].axhline(30, linestyle='--', color='green')
axes[3].set_title('RSI')

# 5. MACD
axes[4].plot(stock_data.index, stock_data['MACD'], label='MACD', color='black')
axes[4].plot(stock_data.index, stock_data['MACD_Signal'], label='MACD Signal', color='red')
axes[4].set_title('MACD & Signal Line')
axes[4].legend()

# 6. Bollinger Bands
axes[5].plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
axes[5].plot(stock_data.index, stock_data['Upper_Band'], label='Upper Band', linestyle='--', color='red')
axes[5].plot(stock_data.index, stock_data['Lower_Band'], label='Lower Band', linestyle='--', color='green')
axes[5].set_title('Bollinger Bands')
axes[5].legend()

# 7. Volume Change
axes[6].plot(stock_data.index, stock_data['Volume_Change'], color='darkblue')
axes[6].set_title('Volume Change')

# 8. Volume Moving Average
axes[7].plot(stock_data.index, stock_data['Volume'], label='Volume', color='gray')
axes[7].plot(stock_data.index, stock_data['Volume_MA_10'], label='10-Day Volume MA', color='orange')
axes[7].set_title('Volume & 10-Day Moving Average')
axes[7].legend()
# ff
plt.tight_layout()
plt.show()
