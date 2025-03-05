import pygame
import random

# Initialize Pygame
pygame.init()

# Maze configuration
rows, cols = 10, 10
cell_size = 40
width, height = rows * cell_size, cols * cell_size

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")

# Grid representation
grid = [[{'visited': False, 'walls': {'top': True, 'right': True, 'bottom': True, 'left': True}}
         for _ in range(cols)] for _ in range(rows)]

# Directions for neighbors
directions = {'top': (0, -1, 'bottom'), 'right': (1, 0, 'left'),
              'bottom': (0, 1, 'top'), 'left': (-1, 0, 'right')}

# Recursive backtracking algorithm
def generate_maze(x, y):
    grid[x][y]['visited'] = True
    neighbors = []
    
    for direction, (dx, dy, opposite) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and not grid[nx][ny]['visited']:
            neighbors.append((nx, ny, direction, opposite))
    
    random.shuffle(neighbors)
    for nx, ny, direction, opposite in neighbors:
        if not grid[nx][ny]['visited']:
            grid[x][y]['walls'][direction] = False
            grid[nx][ny]['walls'][opposite] = False
            generate_maze(nx, ny)

# Draw the maze
def draw_maze():
    for row in range(rows):
        for col in range(cols):
            x, y = col * cell_size, row * cell_size
            if grid[row][col]['walls']['top']:
                pygame.draw.line(screen, BLACK, (x, y), (x + cell_size, y), 2)
            if grid[row][col]['walls']['right']:
                pygame.draw.line(screen, BLACK, (x + cell_size, y), (x + cell_size, y + cell_size), 2)
            if grid[row][col]['walls']['bottom']:
                pygame.draw.line(screen, BLACK, (x, y + cell_size), (x + cell_size, y + cell_size), 2)
            if grid[row][col]['walls']['left']:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + cell_size), 2)

# Generate the maze starting at (0, 0)
generate_maze(0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(WHITE)
    
    # Draw the maze
    draw_maze()
    
    # Update the display
    pygame.display.flip()

pygame.quit()

# This is a test commit I am testing 

# Okay now what about this one 

