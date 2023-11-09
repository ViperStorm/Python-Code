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


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
# game loop
while running:
    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("a keystroke has been pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")

    player(playerX, playerY)

    pygame.display.update()
