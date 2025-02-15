#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((1000,500))
display.set_caption("Shooter")


bot = transform.scale(image.load("bot.png"),(60,60))
fortress = transform.scale(image.load("fortress.png"),(400,400))
graund = transform.scale(image.load("graund.png"),(300,300))
graund1 = transform.scale(image.load("graund.png"),(300,300))
graund2 = transform.scale(image.load("graund.png"),(300,300))
graund3 = transform.scale(image.load("graund.png"),(300,300))
play = transform.scale(image.load("play.png"),(60,60))
menu_fon = transform.scale(image.load("fon.png"),(1000,500))
fon = transform.scale(image.load("fon.png"),(1000,500))




finish = False
menu = 1
level_1=0

fps = 60
clock = time.Clock()

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)





class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
    
    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
            
game = 1

a = Player("hero.png", 50,280,100,80,0,10)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
                        

            
        if level_1:
            wn.blit(graund,(0,200))
            wn.blit(fortress,(500,50))
            wn.blit(graund1,(300,200))
            wn.blit(graund2,(400,200))
            wn.blit(graund3,(700,200))
            wn.blit(bot,(490,270))
            a.show()
            a.move()

        if menu:            
            wn.blit(menu_fon,(1000,500))

            wn.blit(play,(100,100))
            
    display.update()
    clock.tick(fps)
