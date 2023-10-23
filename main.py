import pygame as pg
import random
import math as m

screen = pg.display.set_mode((800, 700))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

class Paddle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.vel = 0

        if (self.y + self.height) > 800:
            self.vel = 0
            self.y = 800

    def draw_paddle(self):
        pg.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.w = width
        self.velx = 3
        self.vely = 5
    
    def draw_ball(self):
        pg.draw.rect(screen, ORANGE, (self.x, self.y, self.w, self.w))

def get_input(user):
    direction = None
    keys = pg.key.get_pressed()
    if keys[pg.K_w] == True:
        if user.y > 0:
            direction = "up"
    elif keys[pg.K_s] == True:
        if user.y < 630:
            direction = "down"
    else:
        direction = "stopped"
        
    return direction



def main():
    player = Paddle(35, 365, 10, 70)
    ball = Ball(390, 340, 20)
    direction = "stopped"
    
    run = True
    while run:
        screen.fill(BLACK)

        player.draw_paddle()
        ball.draw_ball()
        ball_rect = pg.Rect(ball.x, ball.y, ball.w, ball.w)
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)

        vel_change_rate = random.randint(-2, 2)


        ###
        if ball.y < 0:
            ball.vely += -2*(ball.vely)
        elif ball.y > 680:
            ball.vely += -2*(ball.vely)

        if ball.x > 780:
            ball.velx += -2*(ball.velx)
        elif pg.Rect.colliderect(player_rect, ball_rect):
            ball.velx += -2*(ball.velx)
        elif ball.x < 0:
            ball.x, ball.y = 390, 340

        ball.y += ball.vely
        ball.x += ball.velx
        ###

        direction = get_input(player)

        if direction == "up":
            player.y += -6
        elif direction == "down":
            player.y += 6
        elif direction == "stopped":
            player.y += 0


        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
main()

pg.quit()
