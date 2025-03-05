import numpy as np
import matplotlib.pyplot as plt
import random

# Define the grid size and create an empty grid
grid_size = 10
grid = np.zeros((grid_size, grid_size))  # A 10x10 grid initialized with zeros

# Define the robot's start position, pickup locations, and packing station
start_pos = (0, 0)  # Starting point of the robot
pickup_locations = [(2, 3), (4, 7), (7, 2), (8, 8)]  # Locations the robot needs to visit
packing_station = (9, 9)  # The destination (packing station)

# Define obstacles in the grid (represented as -1 in the grid)
obstacles = [(1, 5), (3, 3), (6, 6), (7, 5)]
for obs in obstacles:
    grid[obs] = -1  # Set obstacle positions to -1 to indicate blocked cells

# Function to visualize the current state of the grid
def visualize_grid(path=None):
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='gray_r')  # Display the grid with a grayscale color map

    # Mark obstacles with 'X'
    for obs in obstacles:
        ax.text(obs[1], obs[0], 'X', ha='center', va='center', color='red')
    
    # Mark the start position with 'S'
    ax.text(start_pos[1], start_pos[0], 'S', ha='center', va='center', color='blue')
    
    # Mark pickup locations with 'P'
    for loc in pickup_locations:
        ax.text(loc[1], loc[0], 'P', ha='center', va='center', color='green')
    
    # Mark the packing station with 'D'
    ax.text(packing_station[1], packing_station[0], 'D', ha='center', va='center', color='purple')
    
    # If a path is provided, draw it on the grid
    if path:
        x_coords, y_coords = zip(*path)  # Extract the x and y coordinates from the path
        ax.plot(y_coords, x_coords, marker='o', color='orange')  # Draw the path with orange circles

    plt.show()  # Show the plot

# Function to create an initial random path for the robot
def generate_initial_path():
    # start the path variable to the robot's initla starting position
    path = [start_pos]
    # shuffle the pickup locations randomly and add them to the path array 
    random.shuffle[pickup_locations]
    path.extend[pickup_locations]
    
    path.append(packing_station)
    
    return path  # Return the initial randomly generated path

# Function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # Manhattan distance formula

# Function to calculate the total travel distance of a given path
def calculate_total_distance(path):
    #init total distance
    total_distance = 0
    
    # Call manhatten function
    for i in range(len(path)-1):
        total_distance += manhattan_distance(path[i], path[i+1])
    return total_distance  # Return the total distance

# Function to generate neighboring solutions by swapping the order of two pickup locations
def generate_neighbors(path):
    #TODO
    # extract the pickup locations of the 
    neighbors = []
    pickup_section = path[1:-1]
    # Create new neighbors by swapping each pair of pickup locations
    for i in range(len(pickup_section)):
        for j in range(i+1, len(pickup_section)):
            new_path = path[:]
            new_path[i+1], new_path[j+1] = new_path[j+1], new_path[i+1]
            neighbors.append(new_path)
    return neighbors  # Return the list of neighboring paths

# Hill climbing algorithm implementation
def hill_climbing(initial_path):
    #TODO
    #init
    current_path = initial_path
    current_distance = calculate_total_distance(current_path)
    
    while True:
        neighbors = generate_neighbors(current_path)
        improved = False
        
        # For each neighbor evaluate any improvements
        for neighbor in neighbors:
            # Caslculate the distance of each neighbor path 
            neighbor_distance = calculate_total_distance(neighbor)
            if(neighbor_distance < current_distance): # If the neighbor is better 
                current_path = neighbor # Update the current path to the better neighbor
                current_distance = neighbor_distance # Update the current distance 
                improved = True # Set improved flag to true for finding better neighbor
                visualize_grid(current_path) # Visualization
                break # Move to improved neighbor
            if not improved: # If no improvement found
                break # Terminate loop(local minima reached)
    return current_path, current_distance  # Return the final optimized path and its distance

# Generate the initial random path and visualize it
initial_path = generate_initial_path()
visualize_grid(initial_path)  # Visualize the grid with the initial random path

# Run the hill climbing algorithm and visualize the steps
final_path, final_distance = hill_climbing(initial_path)
print("Final Optimized Path:", final_path)  # Print the final optimized path
print("Final Distance:", final_distance)  # Print the total distance of the optimized path