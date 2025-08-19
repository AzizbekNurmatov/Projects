# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Data Cleaning: Removing rows with missing customer ID and negative quantities
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel(url, engine='openpyxl')
print(df.head())

df.dropna(subset=['CustomerID'], inplace=True)
df = df[df['Quantity'] > 0]

df.info()
df.describe()

# Feature Engineering: Creating features based on customer purchasing behavior
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
customer_data = df.groupby('CustomerID').agg({
    'TotalPrice': 'sum',   # Total money spent by customer
    'InvoiceNo': 'nunique', # Frequency of purchases
    'Quantity': 'sum'       # Total quantity of products purchased
}).reset_index()

print(df.head(5))

# Select the needed features for scaling
numeric_columns = customer_data[['TotalPrice', 'Quantity']]

# Initialize the StandardScaler
scaler_standard = StandardScaler()
# Converts the original values to be on a standard scale 
standard_scaled = scaler_standard.fit_transform(numeric_columns)

scaled_df = pd.DataFrame(standard_scaled, columns=numeric_columns.columns)
print("\nStandard Scaled Data")
print(scaled_df)

# Step 3: Exploring Predictors (Feature Selection with Correlation)
# Checking correlation between features to identify potential predictors
correlation_matrix = customer_data[['TotalPrice', 'InvoiceNo', 'Quantity']].corr()

kmeans = KMeans(n_clusters=2)
kmeans.fit(scaled_df)


# Get cluster labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(scaled_df['TotalPrice'], scaled_df['Quantity'], c=labels, cmap='rainbow')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, marker='X', c='black')
plt.title('K-Means Clustering')
plt.xlabel("Total Price")
plt.ylabel("Quantity")
plt.legend()  
plt.show()

# Compute the mean UnitPrice per customer and align it with customer_data
# Use the 'CustomerID' as the key to ensure alignment
X = customer_data[['CustomerID', 'InvoiceNo', 'Quantity']]
Y = customer_data['TotalPrice']

X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
y_train, y_test = train_test_split(Y, test_size=0.2, random_state=42)

clustering_features = X[['InvoiceNo', 'Quantity']]

# Create KMeans model
kmeans = KMeans(n_clusters=4)
kmeans.fit(clustering_features)

# Get cluster centers and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

X['Cluster'] = labels

# Print cluster centers
print("Cluster Centers:")
print(centroids)
 
# Print the shapes of the training and test sets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and display results
predictions = model.predict(X_test)
print("Predictions:", predictions)

def calculate_mse(actual, predicted):
    # Compute the squared differences between actual and predicted values
    squared_differences = (actual - predicted) ** 2
    # Calculate the average (mean) of squared differences to get MSE
    mse = np.mean(squared_differences)
    return mse

def calculate_rmse(actual, predicted):
    # Calculate MSE and take the square root to get RMSE
    mse = calculate_mse(actual, predicted)
    rmse = np.sqrt(mse)
    return rmse

rmse = calculate_rmse(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(rmse, ' - RMSE Value')
print(mae, ' - MAE Value')
print('Here we can notice that the MAE results better ', end='')
print('when it comes to this customer spending data')

# Plot the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Features')
plt.show()

print(customer_data.head())
