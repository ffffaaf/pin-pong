from pygame import *
from random import *
from time import time as timer
font.init()

window_wight = 700
window_height = 500
font = font.SysFont('Arial' , 40)

window = display.set_mode((window_wight , window_height))
display.set_caption('Pin-Pong')
background = transform.scale(image.load('background.jpg') , (window_wight , window_height))


game = True
clock = time.Clock()
FPS = 40

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
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y  > window_height:
            self.rect.x = randint(80 , window_wight - 80)
            self.rect.y = - 50
            lost = lost + 1

rocket = Player(250 , 100 , 'racket.png' , 3 , 30 , 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    rocket.update()

    display.update()
    clock.tick(FPS)