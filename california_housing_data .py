import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the California Housing dataset from the .data file
# The columns are known from the dataset description, so we specify them manually. 
columns = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
    "Population", "AveOccup", "Latitude", "Longitude"
]

# Load the .data file assuming it is comma-separated
file_path = r"C:\Users\azizb\Documents\CSCI270\cal_housing.data"
data = pd.read_csv(file_path, header=None, names=columns)

# Normalize using Min-Max
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

# Randomly select a house using random seed 42
np.random.seed(42)
random_idx = np.random.randint(0,len(normalized_data))
random_house = normalized_data[random_idx]

# Select a house manually --> Let's use thefirst one 
selected_house = normalized_data[0]

# Euclidean Distance def
def euclidean_dist(vector1, vector2):
    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i]-vector2[i])**2
    return np.sqrt(distance)

# Compute Euclidean distance between selected house andrandomly chosen house
eu_dis = euclidean_dist(random_house,selected_house)

# Plot the normalized data
feature_labels_for_plot = columns

plt.figure(figsize = (10,6))
plt.plot(feature_labels_for_plot, selected_house, marker = 'o',label = "Selected House")
plt.plot(feature_labels_for_plot, random_house, marker = "x", label = "Random House")

plt.title("Cal House Normalized Features")
plt.xlabel("Features")
plt.ylabel("Normalized Values")
plt.xticks(rotation = 45, ha = "right")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Normalized features of the random house ")
print(random_house)
print("\n Normalized features of the manually selected house: ")
print(selected_house)
print(f"\n Euclidean Distance between the two house vectors: {eu_dis:.4f}")