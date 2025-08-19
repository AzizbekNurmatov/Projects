import numpy as np
import random
import matplotlib.pyplot as plt

# Pre-generated perfect maze (0: open space, 1: wall)
maze = np.array([
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
])

# Task 1: Random Initialization of robot and target positions
def random_position(maze):
    while True:
        x, y = random.randint(0, maze.shape[0] - 1), random.randint(0, maze.shape[1] - 1)
        if maze[x, y] == 0:  # Ensure the position is an open space
            return (x, y)

robot_pos = random_position(maze)
target_pos = random_position(maze)

# Task 3: Distance Metrics (Euclidean, Manhattan, Chebyshev)
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def chebyshev_distance(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))

# Task 2: Randomized Obstacles with Dynamic Removal
def modify_random_obstacle(maze):
    x, y = random.randint(0, maze.shape[0] - 1), random.randint(0, maze.shape[1] - 1)
    if random.random() < 0.5:
        # Add an obstacle if it's an open space
        if maze[x, y] == 0:
            maze[x, y] = 1
    else:
        # Remove an obstacle if it's a wall
        if maze[x, y] == 1:
            maze[x, y] = 0

# Task 4: Movement Logic
def move_robot(maze, robot_pos, target_pos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    current_x, current_y = robot_pos
    best_move = None
    min_distance = float('inf')

    # Smart selection of distance metric
    for dx, dy in directions:
        new_x, new_y = current_x + dx, current_y + dy
        if 0 <= new_x < maze.shape[0] and 0 <= new_y < maze.shape[1] and maze[new_x, new_y] == 0:
            # Calculate distances using the actual positions
            euc_dist = euclidean_distance(new_x, new_y, target_pos[0], target_pos[1])
            man_dist = manhattan_distance(new_x, new_y, target_pos[0], target_pos[1])
            che_dist = chebyshev_distance(new_x, new_y, target_pos[0], target_pos[1])

            # Use the best distance (for example, Manhattan in this case)
            if man_dist < min_distance:
                best_move = (new_x, new_y)
                min_distance = man_dist

    return best_move if best_move is not None else robot_pos  # Return new position or stay in place

# Task 5: Visualization of Maze
def visualize_maze(maze, robot_pos, target_pos, step_number):
    maze_copy = maze.copy()
    maze_copy[robot_pos[0], robot_pos[1]] = 2  # Mark robot position
    maze_copy[target_pos[0], target_pos[1]] = 3  # Mark target position
    plt.imshow(maze_copy, cmap="hot", interpolation="nearest")
    plt.title(f"Maze with Robot and Target - Step number: {step_number}")
    plt.show()

# Simulation loop
steps = 0
while robot_pos != target_pos:
    robot_pos = move_robot(maze, robot_pos, target_pos)
    visualize_maze(maze, robot_pos, target_pos, steps)
    modify_random_obstacle(maze)
    steps += 1

print(f"Robot reached the target in {steps} steps!")
