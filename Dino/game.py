#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((1000,500))
display.set_caption("dino")


graund = transform.scale(image.load("graund.png"),(1000,100))

menu_fon = transform.scale(image.load("fon.png"),(1000,500))
fon = transform.scale(image.load("fon.png"),(1000,500))
fon1 = transform.scale(image.load("fon1.png"),(130,50))
fon2 = transform.scale(image.load("fon2.png"),(400,100))
fon3 = transform.scale(image.load("fon3.png"),(90,80))
fon4 = transform.scale(image.load("fon4.png"),(300,90))
lose_fon = transform.scale(image.load("over.png"),(214,28))
font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,70)
label_lose= font1.render(f"Scrore: ",True,(225,225,225))
score = 0
crop_score = 0
score_text= font1.render(f"0{score}",True,(225,225,225))





finish = False
game_over = False
game_win = False
menu =1
level_1=0
game = 1
fps = 60
clock = time.Clock()

class Area():
    def __init__(self,x=0,y=0,width=10,height=10,color = (5,3,4)):
        self.rect = Rect(x,y,width,height)
        self.color = color

    def fill(self):
        draw.rect(wn,self.color,self.rect)

    def change_color(self,new_color):
        self.color = new_color

    def outline(self,thinkss,outcolor):
        draw.rect(wn,outcolor,self.rect,thinkss)
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

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
        self.gravity = 0.8

    def show(self):
        wn.blit(self.image,(self.rect.x,self.rect.y))
        # draw.rect(wn, (255, 0, 0), self.rect, 2)

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def process_jump(self):
        if self.is_jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed <= -13:
                self.is_jumping = False
                self.jump_speed = 20
    
    def move(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.jump()
            


x_fon = 0
dino = Player("dino.png", 50,330,70,80,0,10)
retry = Player("retry.png",290,285,65,65,0,10)
retry_btn = Area(290,285,65,65)

menu = Player("menu.png",393 ,30,300,80,0,10)

play = Player("play.png",20 ,230,300,79,0,10)
play_btn = Area(20 ,230,300,79)

exit = Player("exit.png",20 ,370,300,79,0,10)
exit_btn = Area(20 ,370,300,79)

kaktus = Player("kaktus.png", 850,330,60,80,0,10)
kaktus1 = Player("kaktus.png", 1450,330,60,80,0,10)
kaktus2 = Player("kaktus.png", 1930,330,60,80,0,10)
kaktus3 = Player("kaktus.png", 1850,330,60,80,0,10)
kaktus4 = Player("kaktus.png", 2230,330,60,80,0,10)
rock = Player("stone.png", 750,340,60,80,0,10)
rock1 = Player("stone.png", 1850,340,60,80,0,10)
bird = Player("bird.png",randint(900,1800),80,80,80,0,0)

birds = sprite.Group()
birds.add(bird)
kaktus_group = sprite.Group()
rock_group = sprite.Group()
kaktus_group.add(kaktus)
kaktus_group.add(kaktus1)
kaktus_group.add(kaktus2)
kaktus_group = sprite.Group()
kaktus_group.add(kaktus3)
kaktus_group.add(kaktus4)
rock_group.add(rock)
rock_group.add(rock1)
while game:
    wn.blit(fon,(x_fon,0))
    wn.blit(fon,(x_fon+1000,0))

    for e in event.get():
        if e.type == QUIT:
            game = 0
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            
                x,y = e.pos
                print(x,y)
                if retry_btn.collidepoint(x,y) and game_over:
                        finish = False
                        game_over = False
                        game_win = False
                        menu = 0
                        score = 0
                        level_1=1
                        game = 1
                        dino = Player("dino.png", 50,330,70,80,0,10)
                        kaktus = Player("kaktus.png", 850,330,60,80,0,10)
                        kaktus1 = Player("kaktus.png", 1450,330,60,80,0,10)
                        kaktus2 = Player("kaktus.png", 1530,330,60,80,0,10)
                        kaktus3 = Player("kaktus.png", 1850,330,60,80,0,10)
                        kaktus4 = Player("kaktus.png", 1930,330,60,80,0,10)
                        rock = Player("stone.png", 750,340,60,80,0,10)
                        rock1 = Player("stone.png", 1850,340,60,80,0,10)
                        bird = Player("bird.png",randint(900,1800),75,80,80,0,0)
                        birds = sprite.Group()
                        birds.add(bird)
                        kaktus_group = sprite.Group()
                        kaktus_group.add(kaktus)
                        kaktus_group.add(kaktus1)
                        kaktus_group.add(kaktus2)
                        kaktus_group = sprite.Group()
                        kaktus_group.add(kaktus3)
                        kaktus_group.add(kaktus4)
                        rock_group = sprite.Group()
                        rock_group.add(rock)
                        rock_group.add(rock1)

                if play_btn.collidepoint(x,y) and menu:
                    level_1 = 1
                    menu = 0
                if exit_btn.collidepoint(x,y) and menu:
                    game = 0 

    x_fon -= 3
                        
    if x_fon <= -1000:
        x_fon = 0
    if not finish:
        if menu:
            play_btn.fill()
            exit_btn.fill()
            wn.blit(menu_fon,(0,0))
            menu.show()
            play.show()
            exit.show()

        if level_1:
            score += 0.5
            wn.blit(graund,(x_fon,400))
            wn.blit(graund,(x_fon+ 1000,400))

            wn.blit(fon1,(10,20))
            score_text= font1.render(f"{int(score)}",True,(225,225,225))
            wn.blit(score_text,(100,35))
            wn.blit(label_lose,(20,35))
            birds.draw(wn)
            dino.show()
            dino.move()
            if dino.rect.y < 300:
                dino.rect.y += 4

            for bird in birds:
                bird.rect.x += -12
                if bird.rect.x <= -80:
                    bird.rect.x = randint(900,1800)
                if sprite.spritecollide(dino,birds,True):
                    level_1 = 0
                    game_over = 1

            for kaktus in kaktus_group:
                kaktus.show()
                kaktus.rect.x -= 10

                if kaktus.rect.colliderect(dino.rect):
                    game_over = 1
                    level_1 = 0 

            if kaktus.rect.x < -50:
               kaktus.rect.x = randint(1100,1300) 



            for rock in rock_group:
                rock.show()
                rock.rect.x -= 10

                if rock.rect.colliderect(dino.rect):
                    game_over = 1
                    level_1 = 0 

            if rock.rect.x < -50:
               rock.rect.x = randint(900,1600)  
            

          
        dino.process_jump()
    if game_over:
        retry_btn.fill()

        wn.blit(fon,(x_fon,0))
        wn.blit(fon,(x_fon+1000,0))
        wn.blit(fon2,(280,150))
        wn.blit(lose_fon,(370,185))
        wn.blit(fon3,(280,280))
        retry.show()
        score_text= font2.render(f"Score: {int(score)}",True,(225,225,225))
        wn.blit(fon4,(390,275))
        wn.blit(score_text,(450, 308-13))
    if game_win:
        # wn.blit(fon2,(280,150))
        wn.blit(Win_fon,(400,180))
    display.update()
    clock.tick(fps)