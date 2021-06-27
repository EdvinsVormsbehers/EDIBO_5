import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 700))

# Title and Icon
pygame.display.set_caption("FirstGame")
icon = pygame.image.load('001-leaf.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('butterfly.png')
playerX = 450
playerY = 300
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('tree.png')
enemyX = random.randint(0, 1000)
enemyY = random.randint(0, 700)
enemyX_change = 0
enemyY_change = 0

# Drawing player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Drawing enemy on the screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    # Makes screen black
    screen.fill((0, 128, 0))

#    playerX += 0.2

    for event in pygame.event.get():
        # Makes able to quit the game
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                print("Right arrow is pressed")
            if event.key == pygame.K_UP:
                playerY_change = -0.3
                print("Up arrow is pressed")
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
                print("Down arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been realised")
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("Keystroke has been realised")
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # Creating X boundaries for a player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    # Creating Y boundaries for a player
    if playerY <= 0:
        playerY = 0
    elif playerY >= 636:
        playerY = 636

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
