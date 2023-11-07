import pygame
import sys

# Pygame setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")  # Set the window title

clock = pygame.time.Clock()  # Create a clock object to control the frame rate

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop when the window is closed

    screen.fill((0, 0, 0))  # Fill the screen with a black color (RGB values)

    # Your game logic and drawing code would go here

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()  # Clean up resources
sys.exit()