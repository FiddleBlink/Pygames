import pygame
from pygame.constants import SCRAP_SELECTION

# Initialize the pygame library
pygame.init()

# create the display
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load('pygametut/ufo.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB color scheme (0-255 range)
    screen.fill((0, 0, 0))
    pygame.display.update()
