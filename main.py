import pygame as pg
import random
x=pg.init()

back=(0,255,255)
sn=(0,51,0)
at=(204,0,0)
window=pg.display.set_mode((700,600))
pg.display.set_caption("CATCH IF YOU CAN GAME BY AlinawazHusain")

clock=pg.time.Clock()
attackx=0
attacky=0
gameOver=False
gameQuit=False
snakeX=35
snakeY=45
snakelen=10
snakewid=10
xvel=0
yvel=0
fps=30
attacklen = 10
attackvel = 10
while gameOver==False:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            gameOver=True
        if snakeX<0:
            snakeX=690
        if snakeX>700:
            snakeX=2
        if snakeY<0:
            snakeY=590
        if snakeY>600:
            snakeY=2

        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                xvel=10
                yvel=0
            if event.key==pg.K_DOWN:
                yvel=10
                xvel=0
            if event.key==pg.K_LEFT:
                xvel=-10
                yvel=0
            if event.key==pg.K_UP:
                yvel=-10
                xvel=0
            if event.key==pg.K_SPACE:
                xvel=0
                yvel=0
            if event.key==pg.K_f:
                attackx = random.randint(20, 600)
                attacky=0
                attackvel=10


    if abs(snakeX-attackx)<6 and abs(snakeY-attacky)<6:
        yvel=0
        xvel=0
        attackvel=0


    snakeY=snakeY+yvel
    snakeX=snakeX+xvel
    window.fill(back)
    clock.tick(fps)
    attacky = attacky + attackvel
    pg.draw.rect(window, at, [attackx, attacky, attacklen, attacklen])
    pg.draw.rect(window,sn,[snakeX,snakeY,snakelen,snakewid])
    pg.display.update()

pg.quit()
quit()

