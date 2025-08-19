import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load the dataset
# We assume that the 'house_data.csv' file is in the same directory as this script.
df = pd.read_csv(r'C:\Users\azizb\Documents\CSCI270\house_data.csv')

# Normalize the dataset
# MinMaxScaler scales the data to a range of 0 to 1, which is useful for K-means clustering,
# especially when the features have very different ranges. Here, all features will be transformed to the [0, 1] range.
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Target column (the price of the houses)
# We will use the 'Price' column as our dependent variable, which we are trying to predict.
target = df_normalized['Price']

# Define three distance metrics used for K-Means clustering

# Euclidean distance: Straight-line distance between two points in a multidimensional space.
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Manhattan distance: Sum of the absolute differences between the coordinates.
# Think of it like the distance you'd travel along a grid in a city with square blocks.
def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

# Chebyshev distance: The maximum distance along any coordinate dimension.
# This metric allows diagonal movements and is useful in cases where diagonal distances count the same as straight ones.
def chebyshev_distance(point1, point2):
    return np.max(np.abs(point1 - point2))

# K-Means Clustering function
# This function assigns data points to k clusters based on the provided distance function.
def k_means_clustering(data, k, distance_func):
    # Randomly select k initial centroids from the data points (k = number of clusters)
    centroids = data.sample(n=k).values  # 'sample' selects k random rows
    # Create an array to store the cluster assignment for each point
    clusters = np.zeros(len(data))  # Initialize all clusters to 0

    # Iterate for a fixed number of steps (typically this would stop when centroids converge, but we use 50 iterations)
    for _ in range(50):  # Fixed number of iterations for simplicity
        # Assign each point to the nearest centroid
        for i, point in enumerate(data.values):
            # Calculate the distance from the current point to each centroid
            distances = [distance_func(point, centroid) for centroid in centroids]
            # Assign the point to the cluster with the nearest centroid
            clusters[i] = np.argmin(distances)

        # Update the centroids by calculating the mean of all points in each cluster
        for j in range(k):
            points_in_cluster = data[clusters == j]  # Select points in cluster j
            if len(points_in_cluster) > 0:  # Only update if there are points in the cluster
                centroids[j] = points_in_cluster.mean()  # Update centroid as the mean of all points in the cluster

    # Return the cluster assignments and the final centroids
    return clusters, centroids

# Error calculation function
# This function calculates three error metrics: SSE, MSE, and RMSE
def calculate_errors(actual, clusters):
    # Mean Squared Error (MSE): The average of the squared differences between actual and predicted values.
    mse = mean_squared_error(actual, clusters)
    # Root Mean Squared Error (RMSE): The square root of MSE, providing a sense of how far off the predictions are in real units.
    rmse = sqrt(mse)
    # Sum of Squared Errors (SSE): The total of the squared differences between actual and predicted values. A lower value means better predictions.
    sse = np.sum((actual - clusters) ** 2)
    return sse, mse, rmse

# Define the features to test for prediction
# These are the features we are comparing to see which one best predicts the house price.
features = ['SquareFootage', 'Bedrooms', 'Bathrooms', 'DistanceToSchool']
k = 3  # We are using 3 clusters for K-means

# Create a list to store the error results for each feature and distance metric combination
results = []

# Loop through each feature to test it as a predictor of house price
#TODO