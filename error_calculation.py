# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Simulated data: actual and predicted
actual = np.array([3, -0.5, 2, 7])
predicted = np.array([2.5, 0.0, 2, 8])

# Sum of Squares Error (SSE)
def calculate_sse(actual, predicted):
    # Compute the squared differences between actual and predicted values
    squared_differences = (actual - predicted) ** 2
    # Sum all the squared differences to get SSE
    sse = np.sum(squared_differences)
    return sse

# Mean Square Error (MSE)
def calculate_mse(actual, predicted):
    # Compute the squared differences between actual and predicted values
    squared_differences = (actual - predicted) ** 2
    # Calculate the average (mean) of squared differences to get MSE
    mse = np.mean(squared_differences)
    return mse

# Root Mean Square Error (RMSE)
def calculate_rmse(actual, predicted):
    # Calculate MSE and take the square root to get RMSE
    mse = calculate_mse(actual, predicted)
    rmse = np.sqrt(mse)
    return rmse

# Output the error values
sse = calculate_sse(actual, predicted)
mse = calculate_mse(actual, predicted)
rmse = calculate_rmse(actual, predicted)

print(f"SSE: {sse}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")

# Visualization of actual vs. predicted values
plt.plot(actual, label="Actual", marker='o')
plt.plot(predicted, label="Predicted", marker='x')
plt.title("Actual vs Predicted Values")
plt.xlabel("Data Points")
plt.ylabel("Values")
plt.legend()
plt.show()
