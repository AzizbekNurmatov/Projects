import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

time = np.arange(0, 100, 1)

# First a linear trend is produced
trend = 0.3 * time

# A seasonal component that incoporates sine waves
seasonal = 10 * np.sin(2 * np.pi * time / 25)

# Some random noise is generated to be used with
# the linear trend
noise = np.random.normal(0, 10, len(time))

# All features are combined together to create
# synthetic time period 
timeSeries = trend + seasonal + noise

# A linear regression model is run on the trend
timeReshaped = time.reshape(-1, 1)
model = LinearRegression()
model.fit(timeReshaped, timeSeries)

# Trend prediction
trend = model.predict(timeReshaped)

# Plotting the original time series data 
# along with the fitted trend line
plt.figure(figsize=(12, 6))
plt.plot(time, timeSeries, label='Original', color='red', alpha=0.5)
plt.plot(time, trend, label='Trend Line', color='green', alpha=0.5)
plt.title('Time Series with Trend and Seasonal Component')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()

# Report
# In this program, a synthetic dataset is generated that 
# also incorporates a trend, seasonal component, and some
# artifical noise as well. This data is then run through
# a regression model. We can then observe a trend line 
# once we plot the data along with the trend line. It 
# can be noticed that the trend line provides it's best 
# attempt at averaging all those datapoints together to
# have a line of best fit that throughs through the time
# series data.