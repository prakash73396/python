import pygame
import random
import math


# INITIALIZE THE PROGRAM:

pygame.init()



# CREATE THE SCREEN:
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('Planet.png')
# ADD SOUND:

# PLAYERS X,Y
playersimg = pygame.image.load('spaceship.png')
playerx = 370
playery = 480
player_click = 0


def player():
    screen.blit(playersimg, (playerx, playery))


# CRETAING ENEMEY:

enemeyimg = []
enemeyx = []
enemeyy = []
enemeyx_click = []
enemeyy_click = []
no_of_enemy = 10
for i in range(no_of_enemy):
    enemeyimg.append(pygame.image.load('alien.png'))
    enemeyx.append(random.randint(0, 735))
    enemeyy.append(random.randint(50, 150))
    enemeyx_click.append(3)
    enemeyy_click.append(40)


def enemey(x, y, i):
    screen.blit(enemeyimg[i], (x, y))


# BULLET CREATING
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_click = 0
bullety_click = 10
# 'START' IS DOESN'T SEE TE BUL
# 'SHOOT; IS CURRENTLY SHOOTING
# SCORE:
score=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
def showscore():
    scorevalue=font.render("score:"+str(score),True,(255,255,255))
    screen.blit(scorevalue,(textx,texty))


#GAME OVER


gameover_font=pygame.font.Font('freesansbold.ttf',32)
overx=200
overy=250
def show_gameover():
    gamevalue=gameover_font.render("GAME OVER",True,(255,255,255))
    screen.blit(gamevalue,(overx,overy))

bullet_behaviour = "start"


def bullet(x, y):
    global bullet_behaviour
    bullet_behaviour = "shoot"
    screen.blit(bulletimg, (x + 16, y + 10))


# collision
def iscollision(enemeyx, enemeyy, bulletx, bullety):
    distance = math.sqrt((math.pow((enemeyx - bulletx), 2)) + (math.pow((enemeyy - bullety), 2)))
    if distance < 27:
        return True
    else:
        return False


# CAPTION AND ICON:

pygame.display.set_caption("space game")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

# GAME LOOPS:
running = True
while running:
    # RGB:

    # background image:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # if keystroke are check whether is pressed or released:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_click = -5
            if event.key == pygame.K_RIGHT:
                player_click = 5
            if event.key == pygame.K_SPACE:
                # bullet is going straight :
                if bullet_behaviour is "start":

                    bulletx = playerx
                    bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_click = 0
    # DOESN'T GO OUTSIDE OF THE BOUND
    playerx += player_click
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # ENEMEY DIRECTION
    for i in range(no_of_enemy):
        if  enemeyy[i]>300:
            for j in range(no_of_enemy):
                enemeyy[j]=2000
            show_gameover()
            break

        enemeyx[i] += enemeyx_click[i]
        if enemeyx[i] <= 0:
            enemeyx_click[i] = 2
            enemeyy[i] += enemeyy_click[i]
        elif enemeyx[i] >= 736:
            enemeyx_click[i] = -2
            enemeyy[i] += enemeyy_click[i]

        # collision:
        collision = iscollision(enemeyx[i], enemeyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_behaviour = "start"
            score += 2
            enemeyx[i] = random.randint(0, 735)
            enemeyy[i] = random.randint(50, 150)
        enemey(enemeyx[i], enemeyy[i], i)

    # SHOOTING MOVEMENTS:
    if bullety <= 0:
        bullety = 480
        bullet_behaviour = "start"
    if bullet_behaviour is "shoot":
        bullet(bulletx, bullety)
        bullety -= bullety_click

    player()
    showscore()
    pygame.display.update()
