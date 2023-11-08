import pygame


pygame.init()


# create the screen
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


running = True
# game loop
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB

    player()

    pygame.display.update()
