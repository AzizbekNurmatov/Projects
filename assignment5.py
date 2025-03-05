import numpy as np  # Importing NumPy for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting
from matplotlib.animation import FuncAnimation  # Importing animation function from Matplotlib

def createTable(size):
    table = []
    for i in range(size):
        table.append([])
    return table

def hashFunc(x, a, b, m):
    return ((a * x + b) % m)

def load_factor(count, size):
    return count/size

def rehash(firstTable, a, b, newSize):
    newTable = createTable(newSize)
    for buck in firstTable:
        for value in buck:
            index = hashFunc(value, a, b, newSize)
            newTable[index].append(value)
    return newTable

loadThreshold = 0.75

def insert(table, count, a, b, m, value):
    index = hashFunc(value, a, b, m)
    if value not in table[index]:
        table[index.append(value)]
        count += 1
        if load_factor(count, m) > loadThreshold:
            newSize = m *2
            table = rehash(table, a, b, newSize)
            m = newSize
    return m, table, count

def calcCost(data, a, b, initialSize, loadThreshold=0.75):
    table = createTable(initialSize)
    m = initialSize
    collisions = 0
    count = 0
    rehashCount = 0
    
    for value in data:
        index = hashFunc(value, a, b, m)
        if table[index]:
            collisions += 1
        if value not in table[index]:
            table[index].append(value)
            count+=1
            
        if load_factor(count, m) > loadThreshold:
            rehashCount += 1
            newSize = m *2
            table = rehash(table, a, b, newSize)
            m = newSize
            
    
    collisionRate = collisions / len(data)
    return rehashCount, collisionRate


# Define the objective function
def objective_function(x):
    """Calculate the objective function value for given x."""
    return np.sin(2 * np.pi * x) + 0.1 * (x ** 2)  # Function with multiple hills and valleys

# Define the gradient (derivative) of the objective function for hill climbing
def gradient(x):
    """Compute the derivative of the objective function at point x."""
    return 2 * np.pi * np.cos(2 * np.pi * x) + 0.2 * x  # Derivative of the function

# Hill Climbing Algorithm
def hill_climbing(starting_point, learning_rate, steps):
    """
    Perform hill climbing optimization starting from an initial point.
    
    Args:
    starting_point: Initial point to start the hill climbing algorithm.
    learning_rate: The step size for each iteration.
    steps: Number of iterations to perform.
    
    Returns:
    path: A list of points representing the path taken by the hill climbing algorithm.
    """
    x = starting_point  # Initialize x from the starting point
    path = [x]  # Initialize the path with the starting point

    for _ in range(steps):
        # Calculate gradient at the current point
        grad = gradient(x)
        
        # Update x using the gradient and learning rate (move towards the gradient)
        x += learning_rate * grad
        
        # Append the new point (x) to the path
        path.append(x)
    
    return path  # Return the complete path taken by the algorithm

# Parameters for the hill climbing algorithm
learning_rate = 0.1  # Step size for hill climbing
steps = 100  # Number of iterations (steps)

# Create the range for the x-axis
x = np.linspace(-3, 3, 400)  # Generate 400 points in the x-axis range from -3 to 3
y = objective_function(x)  # Compute the corresponding y-values for each x point

# Set up the figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure with a specific size

# Plot the objective function
ax.plot(x, y, color='blue', label='Objective Function')  # Plot the objective function
ax.set_ylim(-1.5, 3)  # Set y-axis limits for better visibility

# Initialize the scatter plot for the climbing point
scat = ax.scatter([], [], color='red', s=100, label='Current Position')  # Initialize a scatter plot with an empty point

# Create a text annotation object (this will display the current x, y values)
text_annotation = ax.text(-2.5, 2.5, "", fontsize=12, color='black')  # Add text annotation to the plot

# Function to update the animation at each frame
def update(frame):
    """
    Update the scatter plot and the text annotation for each frame in the animation.
    
    Args:
    frame: Current frame number in the animation (represents iteration step).
    
    Returns:
    Updated scatter plot with the new (x) point and updated text annotation.
    """
    # Get the current point in the path
    x_val = path[frame]  # Get x value from the path at the current frame
    y_val = objective_function(x_val)  # Compute the corresponding y value using the objective function
    
    # Update the scatter plot's point position
    scat.set_offsets(np.array([[x_val, y_val]]))  # Set the position of the scatter point
    
    # Update the text annotation with the current x, y values
    text_annotation.set_text(f"x = {x_val:.4f}, f(x) = {y_val:.4f}")
    
    return scat, text_annotation  # Return the updated scatter plot and text annotation

# Function to reset the hill climbing path with a new random starting point
def reset_animation():
    """Reset the hill climbing path by choosing a new random starting point."""
    global path  # Declare path as a global variable so it can be updated

    # Choose a new random starting point in the range [-3, 3]
    starting_point = np.random.uniform(-3, 3)
    
    # Generate the new hill climbing path
    print(f"New Starting Point: x = {starting_point:.4f}")
    path = hill_climbing(starting_point, learning_rate, steps)

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=steps, init_func=reset_animation, interval=200, blit=False, repeat=True)

# Customize the plot with titles and labels
ax.set_title("Hill Climbing on a Function with Multiple Hills and Valleys")  # Title of the plot
ax.set_xlabel("X-axis")  # Label for the x-axis
ax.set_ylabel("f(x)")  # Label for the y-axis
ax.legend()  # Show legend

# Show the plot with the animation
plt.show()