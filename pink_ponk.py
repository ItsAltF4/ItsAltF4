from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pink Ponk game")
background = transform.scale(image.load("background2.png"), (win_width, win_height))
from random import *
class GameSprite(sprite.Sprite):
   #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
player = Player('platform.png', 5,  win_height - 80, 10)
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
player2 = Player2('platform.png', 640,  win_height - 80, 10)
speed_x = 2.5
speed_y = 2.5
class Ball(GameSprite):
    def update(self):
        global speed_x
        global speed_y
        if self.rect.y < 0 or self.rect.y > 425:
            speed_y*=(-1)
        self.rect.x += speed_x
        self.rect.y += speed_y
        if sprite.collide_rect(player2, ball) or sprite.collide_rect(player, ball):
            speed_x*=(-1)
            speed_y*=(-1)
ball = Ball('ball.png', 450, win_height - 475, 3)
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((0,0,0))
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
    display.update()
    clock.tick(FPS)
