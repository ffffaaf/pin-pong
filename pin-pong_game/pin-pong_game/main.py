from pygame import *
from random import *
from time import time as timer
font.init()

window_wight = 700
window_height = 500
font = font.SysFont('Arial' , 40)
text_lose_player_1 = font.render('Первый игрок проиграл!' , True , (180 , 0 , 0))
text_lose_player_2 = font.render('Второй игрок проиграл!' , True , (180 , 0 , 0))

window = display.set_mode((window_wight , window_height))
display.set_caption('Pin-Pong')
background = transform.scale(image.load('background.jpg') , (window_wight , window_height))


game = True
clock = time.Clock()
FPS = 90

class GameSprite(sprite.Sprite):
    def __init__(self , player_x , player_y , player_image , player_speed , size_x , size_y):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image) , (size_x , size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    def update_L(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

ball = GameSprite(0 , 0 , 'tenis_ball.png' , 4 , 50 , 50)
rocket_1 = Player(0 , 245 , 'racket.png' , 4 , 30 , 100)
rocket_2 = Player(670 , 245 , 'racket.png' , 4 , 30 , 100)

speed_x = 3
speed_y = 3
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background , (0 , 0))
        rocket_1.update_L()
        rocket_1.reset()
        rocket_2.update_R()
        rocket_2.reset()
        ball.reset()
        if ball.rect.y > window_height -50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket_1 , ball) or sprite.collide_rect(rocket_2 , ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(text_lose_player_1 , (175 , 200))
            finish = True
        if ball.rect.x > 700:
            window.blit(text_lose_player_2 , (175 , 200))
            finish = True
           

    clock.tick(FPS)
    display.update()

        