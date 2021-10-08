import pygame
from pygame.constants import SCRAP_SELECTION

# Initialize the pygame library
pygame.init()

# create the display
screen = pygame.display.set_mode((800, 600))

# Player
playerimg = pygame.image.load('/Users/akshatsinghal/Downloads/pygamestut/spaceship1.png')
playerx = 370
playery = 480

def player () :
    screen.blit (playerimg,(playerx,playery))

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

    
    player ()
    pygame.display.update()
