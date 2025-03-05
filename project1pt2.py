import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generating a synthetic dataset and 
# adding some noise 
X = np.linspace(0, 10, 100).reshape(-1, 1) 
noise = np.random.normal(0, 1, X.shape[0]).reshape(-1, 1)
y = 3 * X + 7 + noise

# Splitting the dataset into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=42)

# Using the imported linearRegression method to
# train it on the dataset 
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting the values for the test set
predictions = model.predict(X_test)

# Creating an MSE function to calculate the mean
# squared error
def calcMSE(actual, predicted):
    squared_differences = (actual-predicted) ** 2
    mse = np.mean(squared_differences)
    return mse

# print(predictions)
# print(model.coef_)
# print(model.intercept_)

# Calculate the mse itself with the test set
mse = calcMSE(y_test, predictions)

plt.figure(figsize=(10, 12))
plt.scatter(X,y, color='red', label = 'Original Untested Data', alpha=0.5)
plt.plot(X, model.predict(X), color='blue', label='Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title(f'Linear Regression with MSE: {mse:.2f}')
plt.legend()
plt.show()
# Report
# For this model, a linear regression model was run on a
# synthetic dataset that was generated using the random
# library from python. A linear function was then utilized
# taking into account variables y and x along with some
# artificial noise being added. After the model was split
# into 80% training and 20% testing splits, the regression
# model was run on the dataset. A standard MSE formula was
# also used to evaluate it's prediction error. After running
# the model, we can observe that the MSE in every run 
# presents a good fit with minimal prediction error, and our
# line of best fit correlates nicely with the data points. 
# There weren't many challenges besides determing how to 
# add noise to the dataset and how to incorporate that. 
