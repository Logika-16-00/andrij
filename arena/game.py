from pygame import *

wn = display.set_mode((600,600))
display.set_caption("лапки")

fon = transform.scale(image.load("background.jpg"),(600,600))
clock = time.Clock()
Fps = 120
game = 1 
wn.blit(fon,(0,0))
class player(sprite.Sprite):
    def __init__(self,image_player,x,y,size_x,size_y,speed,life):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def show(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))


    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x -= self.speed
        if keys[K_w]:
            self.rect.y += self.speed
        if keys[K_s]:
            self.rect.y += self.speed

hero = player("hero.png",100,140,100,100,3,3)
enemy = player("enemy.png",450,400,100,3,1)
finish = player("treasure.png",300,200,80,50,0,0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0

    hero.show()
    hero.move()


    clock.tick(Fps)
    display.update()