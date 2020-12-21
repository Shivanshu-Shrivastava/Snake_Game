import pygame
import random
import math
from pygame import mixer

pygame.init()
# background
backround = pygame.image.load("bak2.jpg")
# screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("snake")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#backrnd sound

#mixer.music.load("backr.wav")
#mixer.music.play(-1)

# tail






# snake
snakeImg = []
snakeX = []
snakeY = []
snakechan = []
for i in range(20):
    snakeImg.append(pygame.image.load("box.png"))
    snakeX.append(360)
    snakeY.append(300)
    snakechan.append(20)

    # player box
    boxImg = pygame.image.load("box.png")
    boxX = 360
    boxY = 300
    boxchan = 2


def player(x, y):
    screen.blit(boxImg, (x, y))
def tail():

    return True



# collison
def iscollison(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < 47:
        return True


def visible(x, y):
    screen.blit(playerImg, (x, y))
# scroe
scroe=0
font=pygame.font.Font("freesansbold.ttf",50)
def sco():
    scr=font.render("Score: "+str(scroe),True,(255,255,255))
    screen.blit(scr,(0,0))
#game over
game=pygame.font.Font("freesansbold.ttf",70)
def gameover():
    over=game.render("GAME\nOVER",True,(0,155,0))
    screen.blit(over,(200,289))


# fruit
fruitImg = pygame.image.load("apple.png")
fruitX = random.randint(0, 650)
fruitY = random.randint(0, 450)


def fruit(x, y):
    screen.blit(fruitImg, (x, y))


# def up():
#   global playerY
#    for p in range(700):
#      playerY-=20
def second():
    #global d
    #screen.blit(boxImg,(boxX-64*d,boxY))
    return True

v=""
def first():
    global v
    v=second()
#collison loop

def loop(n):
    pass

a=""
d=1
list = [1, 2, 3, 4]
c=0
dikhna=""
state = ""
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backround, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:# or event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                state = "challeft"
            if event.key == pygame.K_RIGHT:
                state = "chalright"
            if event.key == pygame.K_UP:
                state = "chalup"
            if event.key == pygame.K_DOWN:
                state="chaldown"
            if event.key==pygame.K_ESCAPE:
                running=False



    if state == "challeft":
        boxX -= boxchan
    if state == "chalright":
        boxX += boxchan

    if state == "chalup":
        boxY -= boxchan

    if state == "chaldown":
        boxY += boxchan
    #collison
    collison=iscollison(boxX,boxY,fruitX,fruitY)

    if collison is True:
        eat=mixer.Sound("bite.wav")
        eat.play()
        fruitX = random.randint(30, 700)
        fruitY = random.randint(30, 500)
        scroe+=1
        boxchan+=0
        dikhna="ha"
        #a=tail()



    #tail

    if dikhna == "ha":
        first()

        if boxX <= 0:
            # end=mixer.Sound("gamelose.wav")
            # end.play()
            fruitX = 2000

            boxY = 2000

            # boxX=2000
        if fruitX == 2000:
            gameover()
    #else:
    #3   a=False
    dikhna="na"
    if v is True:
        screen.blit(boxImg, (boxX - 64 * d, boxY))
        d+=1



    #boundries
    if boxX>=736 or boxX<=0 or boxY>=536 or boxY<=0:
        #end=mixer.Sound("gamelose.wav")
        #end.play()
        fruitX=2000

        boxY=2000

        #boxX=2000
    if fruitX==2000:
       gameover()
    player(boxX, boxY)
    fruit(fruitX,fruitY)
    sco()

    pygame.display.update()
