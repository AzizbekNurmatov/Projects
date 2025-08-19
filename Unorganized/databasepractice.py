import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv(r'C:\Users\azizb\Documents\CSCI270\Download Data - STOCK_US_XNYS_CSV.csv')

df['Range'] = df['High'] - df['Low']

print(df.head(10))
#print(df.iloc[2:5])
#print(df[(df['High']) > 31])
df['High Eval'] = df.Range.apply(
    lambda x: x * 5
)
print(df.head(10))
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({'x': df['High'], 'y': df['Low']})

# Create a scatter plot
df.plot.scatter(x='x', y='y')

coefficients = np.polyfit(df['x'], df['y'], 1) 
# 1 indicates a linear fit (degree of the polynomial)

poly_function = np.poly1d(coefficients)

plt.plot(df['x'], poly_function(df['x']), color='red') 
plt.show()
