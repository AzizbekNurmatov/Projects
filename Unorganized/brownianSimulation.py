import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as mtick

# Simulation configuration
T = 1.0               # Total time horizon
N = 252               # Number of time steps (e.g., trading days in a year)
dt = T / N            # Time step size
n_paths = 20          # Number of sample paths

# Time vector
t = np.linspace(0, T, N)

# Generate Brownian increments and paths
dW = np.random.normal(0.0, np.sqrt(dt), size=(n_paths, N - 1))
W = np.hstack((np.zeros((n_paths, 1)), np.cumsum(dW, axis=1)))

# Compute average path across simulations
mean_path = np.mean(W, axis=0)
final_vals = W[:, -1]
mu_T = np.mean(final_vals)
sigma_T = np.std(final_vals)

# Color map for visual differentiation
colors = cm.plasma(np.linspace(0, 1, n_paths))

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))
for i in range(n_paths):
    ax.plot(t, W[i], color=colors[i], linewidth=1.4, alpha=0.9)

# Emphasize the average trajectory
ax.plot(t, mean_path, color='black', linewidth=2.2, linestyle='--', label='Average Path')

# Axis labels and title
ax.set_title(r"Simulated Paths of Standard Brownian Motion $W(t)$", fontsize=20, pad=20)
ax.set_xlabel(r"Time $t$", fontsize=14)
ax.set_ylabel(r"Value $W(t)$", fontsize=14)

# Style adjustments
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=T, decimals=0))
ax.tick_params(labelsize=12)
ax.grid(alpha=0.4, linestyle='--')

# Stats annotation
stats_text = '\n'.join((
    rf'$n = {n_paths}$',
    rf'$\mathbb{{E}}[W(T)] = {mu_T:.4f}$',
    rf'$\mathrm{{SD}}[W(T)] = {sigma_T:.4f}$'
))
ax.text(1.02, 0.5, stats_text, transform=ax.transAxes, fontsize=13,
        verticalalignment='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='whitesmoke'))

# Legend
ax.legend(loc='upper left', fontsize=12, frameon=False)

plt.tight_layout()
plt.show()
