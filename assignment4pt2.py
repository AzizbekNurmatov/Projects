# Code for each section 
# Step1: Setup the problem Cities and Distance Calculation

import numpy as np 
import matplotlib.pyplot as plt

# Generate random coordinates for 10 cities 
num_cities = 10
cities = np.random.rand(num_cities, 2) * 100 # Coordinates of cities in a 100x100 grid

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Visualize cities
def visualize_cities(cities):
    plt.scatter(cities[:,0], cities[:,1], color='blue')
    for i, city in enumerate(cities):
        plt.text(city[0], city[1], f"City {i}")
    plt.title("Cities on 2d Plane")
    plt.show()
    
visualize_cities(cities) # Show the initial city layout


# Step 2: **Initial Solution and Cost Function

# Function to generat ea random initl path (a random permutation of cities)
def generate_initial_path():
    return np.random.permutation(num_cities)

# Function to calculate the total distance of a given path
def calculate_total_distance(path, cities):
    total_distance = 0
    for i in range((len(path))-1):
        total_distance += euclidean_distance(cities[path[-1]], cities[path[0]])
        return total_distance
    
# Generate a random initial path and calculate its distance
initial_path = generate_initial_path()
initial_distance = calculate_total_distance(initial_path, cities)
print(f"Initial Path: {initial_path}")
print(f"Initial Distance: {initial_distance}")

#Step 3: **Generate Neighboring Solutions 

# Function to generate a neighboring solution by swapping two cities
def generate_neighbor(path):
    #Create a copy of the current path
    new_path = path.copy()
    # Randomly choose two cities to swap
    i, j = np.random.randint(0, len(path), size=2)
    # Swap cities
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

# Step 4: ** Simulated Annealing Algorithm
import math

# Simulated Annealing Algorithm
def simulated_annealing(cities, initial_path, initial_temp, cooling_rate, min_temp):
    #-----------------init------------------------
    #Start with the initial path
    current_path = initial_path
    #Calculate the distance
    current_distance = initial_distance
    #Init the temperature 
    temp = initial_temp
    #Track the best path found so far 
    best_path = current_path
    #Track the best distance found so far
    best_distance = current_distance
    
    #In a loop (while), we do hill climibg with temperarue till temp cools down
    while temp > min_temp:
        #Generate a new neighbor path
        new_path = generate_neighbor(current_path)
        #Calculate the distance
        new_distance = calculate_total_distance(new_path, cities)
        #Calculate the difference in distance
        delta_distance = new_distance - current_distance 
        
        #Accept the new solutions if it is better or porbaility allows it 
        if delta_distance < 0 or np.random.rand() < math.exp(-delta_distance / temp):
            #Update the new path
            current_path = new_path
            #Update the distance
            current_distance = new_distance
            
        #Update the best path found
        if current_distance < best_distance:
            # Update the best path found so far 
            best_path = current_path
            #Update the best distance so far
            best_distance = current_distance
            
        #Cooldown the temperature by the given cooling rate
        temp -= cooling_rate
        #Viz
        #Visualize_path(current_path, vities)
    #Return the best path and the best found distance 
    return best_path, best_distance 

# Visualization of the path
def visualize_path(path, cities):
    plt.plot(cities[path,0], cities[path, 1], 'ro-', label='Path')
    plt.plot([cities[path[-1], 0], cities[path[0], 0]], [cities[path[-1], 1], cities[path[0], 1]], 'ro-')
    plt.title(f"Current Path (Distance: {calculate_total_distance(path, cities):.2f})")
    plt.show()

best_path, best_distance = simulated_annealing(cities, initial_path, initial_temp=10000, cooling_rate=0.995, min_temp=0.1)
print(f"Best Path: {best_path}")
print(f"Best Distance: {best_distance}")