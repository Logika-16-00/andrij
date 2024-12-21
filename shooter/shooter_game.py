#Створи власний Шутер!

from pygame import *


wn = display.set_mode((700,500))
display.set_caption("лапки")

fon = transform.scale(image.load("galaxy.jpg"),(700,500))
clock = time.Clock()
FPS = 60
finish = 0

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,speed,life):
        super().__init__()
        self.image= transform.scale(image.load(image_player),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] :
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
class Enemy(Player):
    
rocket = Player(310,360,'rocket.png',60,130,5,5)
game = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0

    if not finish:
        wn.blit(fon,(0,0))
        rocket.draw()
        rocket.update()

    display.update()
    clock.tick(FPS)





