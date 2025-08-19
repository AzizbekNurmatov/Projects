import pygame
import pygame_gui
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
NUM_BOIDS = 50
MAX_SPEED = 5
BOID_RADIUS = 5
NEIGHBOR_RADIUS = 50
SEPARATION_WEIGHT = 0.1
COHESION_WEIGHT = 0.01
ALIGNMENT_WEIGHT = 0.05

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Slider controls for cohesion, separation, and alignment
cohesion_slider = pygame_gui.elements.UIHorizontalSlider(
   relative_rect=pygame.Rect((10, HEIGHT - 80), (150, 20)),
   start_value=COHESION_WEIGHT,
   value_range=(0.0, 0.1),
   manager=manager
)

separation_slider = pygame_gui.elements.UIHorizontalSlider(
   relative_rect=pygame.Rect((180, HEIGHT - 80), (150, 20)),
   start_value=SEPARATION_WEIGHT,
   value_range=(0.0, 0.5),
   manager=manager
)

alignment_slider = pygame_gui.elements.UIHorizontalSlider(
   relative_rect=pygame.Rect((350, HEIGHT - 80), (150, 20)),
   start_value=ALIGNMENT_WEIGHT,
   value_range=(0.0, 0.1),
   manager=manager
)

def lerp_color(color1, color2, t):
   r = int(min(max(color1[0] + (color2[0] - color1[0]) * t, 0), 255))
   g = int(min(max(color1[1] + (color2[1] - color1[1]) * t, 0), 255))
   b = int(min(max(color1[2] + (color2[2] - color1[2]) * t, 0), 255))
   return (r, g, b)

class Boid:
   def __init__(self):
       self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
       angle = random.uniform(0, 2 * np.pi)
       self.velocity = np.array([np.cos(angle), np.sin(angle)]) * MAX_SPEED
       self.color = (255, 255, 255)

   def update(self, boids):
       alignment = self.align(boids) * ALIGNMENT_WEIGHT
       cohesion = self.cohere(boids) * COHESION_WEIGHT
       separation = self.separate(boids) * SEPARATION_WEIGHT

       self.velocity += alignment + cohesion + separation
       self.limit_speed()
       self.position += self.velocity
       self.wrap_around_screen()
       self.update_color(boids)

   def align(self, boids):
       neighbors = [b.velocity for b in boids if self.is_neighbor(b)]
       if neighbors:
           avg_velocity = np.mean(neighbors, axis=0)
           return avg_velocity - self.velocity
       return np.zeros(2)

   def cohere(self, boids):
       neighbors = [b.position for b in boids if self.is_neighbor(b)]
       if neighbors:
           avg_position = np.mean(neighbors, axis=0)
           return avg_position - self.position
       return np.zeros(2)

   def separate(self, boids):
       close_boids = [self.position - b.position for b in boids if self.is_too_close(b)]
       if close_boids:
           return np.sum(close_boids, axis=0)
       return np.zeros(2)

   def is_neighbor(self, other_boid):
       return np.linalg.norm(self.position - other_boid.position) < NEIGHBOR_RADIUS

   def is_too_close(self, other_boid):
       distance = np.linalg.norm(self.position - other_boid.position)
       return 0 < distance < BOID_RADIUS * 2

   def limit_speed(self):
       speed = np.linalg.norm(self.velocity)
       if speed > MAX_SPEED:
           self.velocity = (self.velocity / speed) * MAX_SPEED

   def wrap_around_screen(self):
       if self.position[0] > WIDTH: self.position[0] = 0
       elif self.position[0] < 0: self.position[0] = WIDTH
       if self.position[1] > HEIGHT: self.position[1] = 0
       elif self.position[1] < 0: self.position[1] = HEIGHT

   def update_color(self, boids):
       neighbors = [b.velocity for b in boids if self.is_neighbor(b)]
       if neighbors:
           avg_velocity = np.mean(neighbors, axis=0)
           alignment_score = np.linalg.norm(avg_velocity - self.velocity) / MAX_SPEED
           self.color = lerp_color((0, 255, 0), (255, 0, 0), alignment_score)

   def draw(self):
       pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), BOID_RADIUS)

# Initialize boids
boids = [Boid() for _ in range(NUM_BOIDS)]

# Main loop
running = True
while running:
   time_delta = clock.tick(30) / 1000.0  # Calculate time delta for GUI updates
   screen.fill((0, 0, 0))  # Clear screen with black background

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       manager.process_events(event)

   # Update slider values in real-time
   COHESION_WEIGHT = cohesion_slider.get_current_value()
   SEPARATION_WEIGHT = separation_slider.get_current_value()
   ALIGNMENT_WEIGHT = alignment_slider.get_current_value()

   # Update and draw each boid
   for boid in boids:
       boid.update(boids)
       boid.draw()

   # Update GUI manager and draw GUI
   manager.update(time_delta)
   manager.draw_ui(screen)

   pygame.display.flip()  # Refresh display

pygame.quit()

