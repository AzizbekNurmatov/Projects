import pygame  # Import Pygame for creating visual simulations
import random  # Import random for generating initial positions and angles
import numpy as np  # Import numpy for mathematical operations

# Define constants for simulation
WIDTH, HEIGHT = 800, 600  # Screen dimensions
NUM_BOIDS = 50  # Number of boids in the simulation
MAX_SPEED = 5  # Maximum speed of a boid
BOID_RADIUS = 5  # Radius of each boid
NEIGHBOR_RADIUS = 50  # Radius within which a boid considers others as neighbors
ALIGNMENT_FACTOR = 0.05  # Weight for alignment behavior
COHESION_FACTOR = 0.01  # Weight for cohesion behavior
SEPARATION_FACTOR = 0.1  # Weight for separation behavior

# Initialize Pygame
pygame.init()  # Initialize Pygame components
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create screen with given dimensions
clock = pygame.time.Clock()  # Create clock for managing frame rate


# Define Boid class with position and movement
class Boid:
    def __init__(self):
        # Initialize boid position randomly within screen
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
        # Set initial velocity with random direction and max speed
        angle = random.uniform(0, 2 * np.pi)  # Random angle
        self.velocity = np.array([np.cos(angle), np.sin(angle)]) * MAX_SPEED  # Set velocity vector

    # Move boid based on nearby boids (swarm behavior)
    def move(self, boids):
        # Alignment: Adjust velocity to match the average velocity of neighbors
        avg_velocity = np.mean([b.velocity for b in boids if np.linalg.norm(self.position - b.position) < NEIGHBOR_RADIUS], axis=0)
        alignment = (avg_velocity - self.velocity) * ALIGNMENT_FACTOR if avg_velocity is not None else np.zeros(2)

        # Cohesion: Move towards the average position of neighbors
        avg_position = np.mean([b.position for b in boids if np.linalg.norm(self.position - b.position) < NEIGHBOR_RADIUS], axis=0)
        cohesion = (avg_position - self.position) * COHESION_FACTOR if avg_position is not None else np.zeros(2)

        # Separation: Move away from nearby boids that are too close
        separation = np.sum([self.position - b.position for b in boids if 0 < np.linalg.norm(self.position - b.position) < BOID_RADIUS], axis=0) * SEPARATION_FACTOR

        # Update velocity by combining alignment, cohesion, and separation forces
        self.velocity += alignment + cohesion - separation
        if np.linalg.norm(self.velocity) > MAX_SPEED:  # Limit speed to max speed
            self.velocity = (self.velocity / np.linalg.norm(self.velocity)) * MAX_SPEED
        self.position += self.velocity  # Update position based on velocity

        # Screen wrapping: If boid moves off screen, it reappears on the opposite side
        if self.position[0] > WIDTH: self.position[0] = 0
        if self.position[0] < 0: self.position[0] = WIDTH
        if self.position[1] > HEIGHT: self.position[1] = 0
        if self.position[1] < 0: self.position[1] = HEIGHT

    # Draw boid on the screen
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0]), int(self.position[1])), BOID_RADIUS)

# Initialize a list of boids
boids = [Boid() for _ in range(NUM_BOIDS)]  # Create list of Boid objects

# Main loop for simulation
running = True  # Set running flag to True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black background
    for event in pygame.event.get():  # Process Pygame events
        if event.type == pygame.QUIT:  # Check if quit event has occurred
            running = False  # End the simulation

    # Update each boid's position and draw it
    for boid in boids:
        boid.move(boids)  # Move boid based on other boids
        boid.draw()  # Draw boid on screen

    pygame.display.flip()  # Update the display with new positions
    clock.tick(30)  # Limit frame rate to 30 FPS

pygame.quit()  # Quit Pygame after loop ends
