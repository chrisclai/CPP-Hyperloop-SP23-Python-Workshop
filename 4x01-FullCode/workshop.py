import pygame
import random
import math
from pygame import mixer

#Initialize
pygame.init()

#create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#caption and icon
pygame.display.set_caption("Hyperloop Invaders")

#put references for sprites
player = pygame.transform.scale(pygame.image.load('assets/img/robotics_transparent.png'), (75, 75))
enemy = pygame.transform.scale(pygame.image.load('assets/img/hyperloop_transparent.png'), (150, 100))
bullet = pygame.transform.scale(pygame.image.load('assets/img/yellow_laser.png'), (50, 50))

#Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.Font('freesansbold.ttf', 20)

#Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Points: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over():
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (190, 250))

# Background Sound
mixer.music.load('assets/sfx/background_track.mp3')
mixer.music.play(-1)

# Player
playerImage = player
player_X = 370
player_Y = 500
player_Xchange = 0

# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
    invaderImage.append(enemy)
    invader_X.append(random.randint(64, 737))
    invader_Y.append(random.randint(30, 180))
    invader_Xchange.append(1.2)
    invader_Ychange.append(50)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
bulletImage = bullet
bullet_X = 0
bullet_Y = 500
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

def player(x,y):
    screen.blit(playerImage, (x-16, y+10))

def invader(x,y,i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x,y):
    global bullet_state
    screen.blit(bulletImage, (x,y))
    bullet_state = "fire"

running = True
while running:

    show_score(scoreX, scoreY)
    pygame.display.update()