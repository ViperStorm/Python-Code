import pygame


pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB
    screen.fill((0, 0, 0))
    pygame.display.update()
