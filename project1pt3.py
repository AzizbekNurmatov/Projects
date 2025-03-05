import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate the synthetic dataset with three distinc clusters
X, y = make_blobs(n_samples=500, centers=3, cluster_std=0.5, random_state=0)


# Apply the imported k-means method to 
# the dataset and get it's centroids
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualize all the centroids on a graph
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, marker='X', c='black')
plt.title('K-Means Clustering')
plt.show()

# Report
# In this program, a synthetic data set is first produced
# with the make_blobs method that generated three synthetic
# clusters to be used by the K-Means clustering mdoel. The
# dataset is then passed into the imported KMeans method 
# for it to apply K-Means clustering on using three clusters
# as the base for making our centroids. We can then observe
# that the model accuratey determins the three clusters and 
# appropriately clusters the groups together relative to how
# close the data points are spatially with each other. 