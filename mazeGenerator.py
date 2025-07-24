import tkinter as tk
import random

# Constants for the maze size
MAZE_WIDTH = 20
MAZE_HEIGHT = 20
CELL_SIZE = 30

# Directions for moving in the maze (right, down, left, up)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Maze Generation Function (Recursive Backtracking)
def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    # Stack for backtracking
    stack = []
    
    # Randomly pick a starting point
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    
    # Mark the starting point as a path
    maze[start_y][start_x] = ' '
    
    # Push the start cell onto the stack
    stack.append((start_x, start_y))
    
    # Function to shuffle directions to ensure randomness
    def shuffle_directions():
        return random.sample(DIRECTIONS, len(DIRECTIONS))
    
    # Backtracking algorithm
    while stack:
        x, y = stack[-1]
        directions = shuffle_directions()
        moved = False
        
        # Try each direction
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                # Carve a path
                maze[ny][nx] = ' '
                maze[y + dy][x + dx] = ' '  # Connect the current cell to the next
                stack.append((nx, ny))
                moved = True
                break
        
        if not moved:
            stack.pop()  # Backtrack if no valid move

    return maze

# Drawing the maze on the GUI
def draw_maze(maze):
    root = tk.Tk()
    root.title("Maze Generator")

    canvas = tk.Canvas(root, width=MAZE_WIDTH * CELL_SIZE, height=MAZE_HEIGHT * CELL_SIZE)
    canvas.pack()

    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            color = 'white' if maze[y][x] == ' ' else 'black'
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=color, outline='gray')

    root.mainloop()

# Generate the maze and draw it
maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
draw_maze(maze)
