# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt

# 1. Data Loading
wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

# Convert to DataFrame
X_df = pd.DataFrame(X, columns=feature_names)
y_df = pd.DataFrame(y, columns=['Cultivar'])
print("First 5 rows of the dataset:")
print(X_df.head())
print("\nTarget variable counts:")
print(y_df['Cultivar'].value_counts())

# Provided columns for the given data set
data = pd.DataFrame({
    'Cultivar': ['Alcohol', 'Malic Acid', 'Alcalinity', 'Magnesium',
                    'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins',
                    'Color Intensity', 'Hue', 'OD280/OD315', 'Proline']})
print("Original Data:")
print(data)

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the data
encoded_data = encoder.fit_transform(data[['Cultivar']])

# Get feature names
feature_names = encoder.get_feature_names_out(['Cultivar'])

# Create a DataFrame with the encoded data
encoded_df = pd.DataFrame(encoded_data,columns=feature_names)

print("\nOne-Hot Encoded Data:")
print(encoded_df)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(X_df)

feature_names = list(X_df.columns)
  
# Create a DataFrame with the scaled data
scaled_df = pd.DataFrame(scaled_data, columns=feature_names)

print("\nMin-Max Scaled Data:")
print(scaled_data)

# Initialize the StandardScaler
scaler_standard = StandardScaler()
# Converts the original values to be on a standard scale 
X_standard_scaled = scaler_standard.fit_transform(X_df)

print("\nStandard Scaled Data")
print(X_standard_scaled)

# Translates the target variable to get it's reciprocal values
X_df['Reciprocal_Alcohol'] = 1 / X_df['alcohol']

plt.figure(figsize=(14,6))

# Original distributions for target variables 

# Original Malic Acid Distribution
plt.subplot(2, 3, 1)
plt.hist(X_df['malic_acid'], bins=5, color='skyblue', edgecolor='black')
plt.title('Original Malic Acid Distribution')
plt.xlabel('Malic Acid')
plt.ylabel('Value')

# Original Ash Distribution
plt.subplot(2, 3, 2)
plt.hist(X_df['ash'], bins=5, color='skyblue', edgecolor='black')
plt.title('Original Ash Distribution')
plt.xlabel('Ash')
plt.ylabel('Value')

# Original Alcohol Distribution
plt.subplot(2, 3, 3)
plt.hist(X_df['alcohol'], bins=5, color='skyblue', edgecolor='black')
plt.title('Original Alcohol Distribution')
plt.xlabel('Alcohol')
plt.ylabel('Value')


# All plotted values after proper scaling and transformations

# Malic Acid distribution after min-max scaling
# Transformed the features by scaling each of them to a specified range
plt.subplot(2, 3, 4)
plt.hist(scaled_df['malic_acid'], bins=5, color='red', edgecolor='black')
plt.title('Malic Acid Feature after Min-Max Scaling')
plt.xlabel('Malic Acid')
plt.ylabel('Value')

# Ash distribution after standard scaling 
# 
plt.subplot(2, 3, 5)
plt.hist(X_standard_scaled['ash'], bins=5, color='red', edgecolor='black')
plt.title('Ash Feature after Standard Min-Max Scaling')
plt.xlabel('Ash')
plt.ylabel('Value')

# Alcohol distribution after recipricol transformation
plt.subplot(2, 3, 6)
plt.hist(X_df['Reciprocal_Alcohol'], bins=5, color='red', edgecolor='black')
plt.title('Alcohol Feature after Reciprocal Transformation')
plt.xlabel('Alcohol')
plt.ylabel('Value')

def equilateral_encode(n_classes):
    """
    Generates equilateral encoding vectors for n_classes.
    """
    if n_classes < 2:
        raise ValueError("Number of classes must be at least 2.")
        
    eq_matrix = np.zeros((n_classes, n_classes - 1))
    for i in range(1, n_classes):
        r = np.sqrt(i * (i + 1))
        eq_matrix[:i, i - 1] = -1 / i
        eq_matrix[i, i - 1] = i
        eq_matrix[:i, :i] *= np.sqrt((i**2 + i) / (i**2 + i + 1))
    return eq_matrix

# Define categories
categories = ['Alcohol', 'Malic Acid', 'Alcalinity', 'Magnesium',
                    'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins',
                    'Color Intensity', 'Hue', 'OD280/OD315', 'Proline']
n_classes = len(data)

# Generate Equilateral Encodings
encoding = equilateral_encode(n_classes)

# Create a DataFrame
encoding_df = pd.DataFrame(encoding, columns=[f'Feature_{i+1}' for i in range(n_classes - 1)])
encoding_df['Cultivar'] = categories

print("Equilateral Encoded Data:")
print(encoding_df)


from mpl_toolkits.mplot3d import Axes3D

# Extract features
features = encoding_df[[f'Feature_{i+1}' for i in range(n_classes - 1)]].values

# Plotting
fig = plt.figure(figsize=(8, 6))

if n_classes - 1 == 2:
    # 2D Plot
    plt.scatter(features[:,0], features[:,1])

    for i, txt in enumerate(categories):
        plt.annotate(txt, (features[i,0], features[i,1]))

    plt.title('Equilateral Encoding (2D)')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    
elif n_classes - 1 == 3:
    # 3D Plot
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(features[:,0], features[:,1], features[:,2])

    for i, txt in enumerate(categories):
        ax.text(features[i,0], features[i,1], features[i,2], txt)

    ax.set_title('Equilateral Encoding (3D)')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Feature 3')

plt.tight_layout()
plt.show()