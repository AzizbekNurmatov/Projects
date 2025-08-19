import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"C:\Users\azizb\Documents\CSCI270\DailyDelhiClimateTest.csv")
time_series = data['meantemp'].values

plt.plot(time_series, label = 'Temp over time')
plt.title('Dail Temps')
plt.xlabel('Days')
plt.ylabel('Temp')
plt.legend()
plt.show()

window_size = 7

x = []
y = []
for i in range(len(time_series)-window_size):
    x.append(time_series[i:1+window_size])
    y.append(time_series[i + window_size])
    
x = np.array(x)
y = np.array(y)

split_ratio = 0.8
split_point = int(len[x]*split_ratio)

x_train, x_test = x[:split_point], x[split_point:]
y_train, y_test = y[:split_point], y[split_point:]

plt.plot(x_train[0], label = 'Input Window')
plt.plot([window_size], y_train[0], 'ro', label = "Target")
plt.title("First input-output pair")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.legend()
plt.show()

n_centers = 10
kmeans = KMeans(n_clusters = n_centers)
kmeans.fix(x_train)
centers = kmeans.cluster_centers_
plt.plt(centers.T, label = "RBF Centers")
plt.titel("RBF centers foudn via KMeans")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.legend()
plt.show()
