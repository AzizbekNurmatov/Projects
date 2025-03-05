# Write a report explaining yoiuyr approach, findings, and visualizations 
# Add comments
# On the report, include a discussiojn on the model's performance
# and any challenges you encountered
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the iris dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Slitting the dataset into training and testing sets
X_train, X_test = train_test_split(x, test_size=0.2, random_state=42)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=42)

# Using imported KNN method to train on the dataset
knnclassifier = KNeighborsClassifier(n_neighbors=3)
knnclassifier.fit(X_train, y_train)

# Predicting the species of the flowers 
y_pred = knnclassifier.predict(X_test)

# Print out necessary metrics to get a better
# idea of the data
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

featureX = iris.data[:,0]
featureY = iris.data[:,1]
species = iris.target

colors = ['red', 'blue', 'green']
species_names = iris.target_names

# Modify database to visualize the graph that creates 
# clusters of the flowers in different colors
plt.figure(figsize = (10,12))

i = 0
for color in colors:
    print(f"Index: {i}, Color: {color}")
    plt.scatter(
        featureX[species==i],
        featureY[species==i],
        label = species_names[i], 
        color=color,
        alpha= 0.5
    )
    i += 1
    
plt.title("Classification with the Iris Dataset: ", fontsize=15)
plt.xlabel("Sepal Length: ", fontsize=15)
plt.ylabel("Sepal Width: ", fontsize=15)
plt.legend(title="Species", fontsize=12)
plt.tight_layout()
plt.show()

# Report
# The widely used Iris data set was classified and clustered 
# into three groups via the K-Nearest Neighbors algorithm.
# The KNN model was run on an 80% training and 20% testing
# set. The performance of the used KNN model was evaluated
# based on how well it had classified the three different 
# groups we had set the model too. It assigns each of the 
# data points with a different color to create it's
# distinction as being part of one group or another. One 
# challenge was trying to ensure that all the data points
# were being optimally visuzlized for whatever group they
# fell into. 