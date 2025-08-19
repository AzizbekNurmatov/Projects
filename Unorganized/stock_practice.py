import pandas as pd
import matplotlib.pyplot as plt
stock = pd.read_csv('GOOG.csv')
print(stock.head())

# Sets date column in the format of a datetime data type and sets it as index
stock['Date'] = pd.to_datetime(stock['Date'])
stock.set_index('Date', inplace=True)


# stock['daily_average'] = stock['Close'].resample('W').mean()
# plt.plot(stock['daily_average'])
# plt.show()
# print(stock.head())
#------------------------------------------------------------------------------------------
import bt 
import matplotlib.pyplot as plt  
bt_data = bt.get('goog, amzn, nvda', start='2023-1-1', end='2025-1-1')
print(bt_data.head())

bt_strategy = bt.Strategy('Trade_Weekly',
                          [bt.algos.RunWeekly(), # Run weekly
                           bt.algos.SelectAll(), # Use all data 
                           bt.algos.WeighEqually(), # Maintain equal weights
                           bt.algos.Rebalance()]) # Rebalance 

# Create a backtest
bt_test = bt.Backtest(bt_strategy, bt_data)

# Run the backtest
bt_res = bt.run(bt_test)

print(bt_res.display())

# Plot the result 
bt_res.plot(title='Backtest Result')
plt.show()
bt_res.get_transactions()
#------------------------------------------------------------------------------------------
# import talib 

# stock['SMA_short'] = talib.SMA(stock['Close'], timeperiod=10)
# stock['SMA_long'] = talib.SMA(stock['Close'], timeperiod=50)

# stock['EMA_short'] = talib.EMA(stock['Close'], timeperiod=10)
# stock['EMA_long'] = talib.EMA(stock['Close'], timeperiod=50)

# plt.plot(stock['SMA_short'], label = 'SMA_short')
# plt.plot(stock['SMA_long'], label = 'SMA_long')
# plt.plot(stock['EMA_short'], label = 'EMA_short')
# plt.plot(stock['EMA_long'], label = 'EMA_long')
# plt.plot(stock['Close'], label = 'Close')

# plt.legend()
# plt.title('EMAs and SMAs')
# plt.show()
#------------------------------------------------------------------------------------------
