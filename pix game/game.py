#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((1000,500))
display.set_caption("Shooter")


gem = transform.scale(image.load("gem.png"),(30,30))
gem = transform.scale(image.load("gem.png"),(30,30))
gem = transform.scale(image.load("gem.png"),(30,30))
gem = transform.scale(image.load("gem.png"),(30,30))
gem = transform.scale(image.load("gem.png"),(30,30))
graund = transform.scale(image.load("graund.png"),(300,300))
graund1 = transform.scale(image.load("graund.png"),(300,300))
graund2 = transform.scale(image.load("graund.png"),(300,300))
graund3 = transform.scale(image.load("graund.png"),(300,300))
menu_fon = transform.scale(image.load("fon.png"),(1000,500))
fon = transform.scale(image.load("fon.png"),(1000,500))
fon1 = transform.scale(image.load("fon1.png"),(130,50))
font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)
label_lose= font1.render(f"Gem: ",True,(225,225,225))
score= font1.render(f"0",True,(225,225,225))




finish = False
menu = 0
level_1=1

fps = 60
clock = time.Clock()



class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life
        self.is_jumping = False
        self.jump_speed = 20
        self.gravity = 10

    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True    
    def process_jump(self):
        if self.is_jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed <= -45:
                self.is_jumping = False
                self.jump_speed = 40
    
    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.jump()

            
game = 1
gems = sprite.Group()
gems.add(gem)
a = Player("hero.png", 50,200,100,80,0,10)
gen = Player("hero.png",0,0,0,0)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    
                        


    if not finish:
        if menu:
            wn.blit(menu_fon,(0,0))

        if level_1:
            wn.blit(graund,(0,200))
            wn.blit(graund1,(300,200))
            wn.blit(graund2,(400,200))
            wn.blit(graund3,(700,200))
            wn.blit(gem,(400,300))
            wn.blit(fon1,(10,20))
            wn.blit(score,(80,35))
            wn.blit(label_lose,(20,35))
            a.rect.x+=5
            a.show()
            a.move()

            if sprite.spritecollide(a,gens,True):
                print(4)
    a.process_jump()

            
    display.update()
    clock.tick(fps)