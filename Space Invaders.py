import pygame
import math
import random

# Initialize the pygame library
pygame.init()

# create the display
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('pygametut/back.jpg')
background = pygame.transform.scale(background, (800, 600))

# MIT LOGO
mit = pygame.image.load('pygametut/MIT.png')
mit = pygame.transform.scale(mit, (250, 75))

# Player
playerimg = pygame.image.load('pygametut/spaceship1.png')
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0

def player(x, y):
    screen.blit(playerimg, (x, y))


# Alien
alienimg = []
alienx = []
alieny = []
alienx_change = []
alieny_change = []
no_of_aliens = 5

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load('pygametut/ufo1.png'))
    alienx.append(random.randint(0, 735))
    alieny.append(random.randint(50, 150))
    alienx_change.append(0.5)
    alieny_change.append(40)


def alien(x, y, i):
    screen.blit(alienimg[i], (x, y))


# Bullet
bulletimg = pygame.image.load('pygametut/bullet.png')
bulletimg = pygame.transform.rotate(bulletimg, 45)
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 1.5
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.Font('pygametut/Margarine-Regular.ttf', 32)

textx = 10
texty = 10

# Game over Text
over_font = pygame.font.Font('/Users/akshatsinghal/Downloads/pygamestut/Margarine-Regular.ttf', 70)
over_font1 = pygame.font.Font('/Users/akshatsinghal/Downloads/pygamestut/Margarine-Regular.ttf', 30)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    over_text1 = over_font1.render("Made By :", True, (255, 255, 255))
    screen.blit(over_text1, (0, 400))
    over_text2 = over_font1.render("Akshat Singhal", True, (255, 255, 255))
    screen.blit(over_text2, (0, 430))
    over_text3 = over_font1.render("Parth Bangde", True, (255, 255, 255))
    screen.blit(over_text3, (0, 460))
    over_text4 = over_font1.render("Yash Nandankar", True, (255, 255, 255))
    screen.blit(over_text4, (0, 490))
    over_text5 = over_font1.render("Aryan Kumar Prasad", True, (255, 255, 255))
    screen.blit(over_text5, (0, 520))
    over_text6 = over_font1.render("Priti Chaudhari", True, (255, 255, 255))
    screen.blit(over_text6, (0, 550))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))


def isCollision(alienx, alieny, bulletx, bullety):
    distance = math.sqrt((math.pow(alienx-bulletx, 2)) +
                         (math.pow(alieny-bullety, 2)))
    if distance < 25:
        return True
    else:
        return False


#title and icon
pygame.display.set_caption("Space Invasion @ MitWpu")
icon = pygame.image.load('pygametut/ufo.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(mit, (520, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1
            if event.key == pygame.K_RIGHT:
                playerx_change = 1
            if event.key == pygame.K_UP:
                playery_change = -1
            if event.key == pygame.K_DOWN:
                playery_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # gets the current x cord of player
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0
    playerx += playerx_change
    playery += playery_change

    # boundry of movement of the player
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # movement of alien UFO
    for i in range(no_of_aliens):

        # Game Over
        if alieny[i] > 440:
            for j in range(no_of_aliens):
                alieny[j] = 2000
            playery = 2000
            game_over_text()
            break
            
        collision = isCollision(alienx[i], alieny[i], playerx, playery)
        if collision:
            for j in range(no_of_aliens):
                alieny[j] = 2000
            playery = 2000
            bossy = 2000
            game_over_text()
            break

        alienx[i] += alienx_change[i]
        if alienx[i] <= 0:
            alienx_change[i] = 0.5
            alieny[i] += alieny_change[i]
        elif alienx[i] >= 736:
            alienx_change[i] = -0.5
            alieny[i] += alieny_change[i]

        # collision
        collision = isCollision(alienx[i], alieny[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            alienx[i] = random.randint(0, 735)
            alieny[i] = random.randint(50, 350)

        alien(alienx[i], alieny[i], i)

    # Movement of Bullet
    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
