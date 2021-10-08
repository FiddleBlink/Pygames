import pygame

# Initialize the pygame library
pygame.init()

# create the display
screen = pygame.display.set_mode((800, 600))

# Player
playerimg = pygame.image.load('/Users/akshatsinghal/Downloads/pygamestut/spaceship1.png')
playerx = 370
playery = 480
playerx_change = 0

def player (x,y) :
    screen.blit (playerimg,(x,y))

# Alien
alienimg = pygame.image.load('/Users/akshatsinghal/Downloads/pygamestut/ufo1.png')
alienx = 370
alieny = 50
alienx_change = 0

def alien (x,y) :
    screen.blit (alienimg,(x,y))

#title and icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load('/Users/akshatsinghal/Downloads/pygamestut/ufo.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                playerx_change = -0.5
            if event.key == pygame.K_RIGHT :
                playerx_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerx_change = 0
    playerx += playerx_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736 :
        playerx = 736
    
    player (playerx,playery)
    alien (alienx,alieny)
    pygame.display.update()
