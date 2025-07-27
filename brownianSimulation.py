import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1.0         # Total time (e.g., 1 year)
N = 252         # Number of steps (e.g., trading days)
dt = T / N      # Time step
n_paths = 10    # Number of paths to simulate

# Brownian Motion paths
t = np.linspace(0, T, N)
dW = np.random.normal(scale=np.sqrt(dt), size=(n_paths, N-1))
W = np.hstack((np.zeros((n_paths, 1)), np.cumsum(dW, axis=1)))  # Start at 0

# Plot
plt.figure(figsize=(10, 6))
for i in range(n_paths):
    plt.plot(t, W[i], lw=1)
plt.title("Simulated Paths of Standard Brownian Motion")
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.grid(True)
plt.show()
