import pygame


pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invaders")


running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
