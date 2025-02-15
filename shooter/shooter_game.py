#Створи власний Шутер!

from pygame import *
from random import *
from time import time as timer
wn =  display.set_mode((700,500))
display.set_caption("Shooter")

fon = transform.scale(image.load("galaxy.jpg"),(700,500))
finish = False
fps = 60
clock = time.Clock()


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")

font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,80)
lose = 0 #збито
catch = 0 #пропущен

label_lose= font1.render(f"Пропущено {lose}",False,(193,17,11))
                        
label_catch= font1.render(f"Збито {catch}",False,(13,197,11))
  
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
            
        if keys[K_w]:
            self.fire()
            
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.x+15+7,self.rect.y,15,15,0,randint(8,15))
        bullets.add(bullet)
bullets = sprite.Group()


class Enemy(Player):
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -10
            self.rect.x = randint(0,650)
            self.speed = randint(1,5)
            lose +=1
            
class Bullet(Player):
    def update(self):
        if self.rect.y < 0:
            self.kill()
        self.rect.y -= 5
        
        
        
        
    



rocket = Player("rocket.png",310,360,  60,130,5,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(0,650), 0,90,60,randint(1,5),randint(1,5))
    monsters.add(enemy)
    
asteroids = sprite.Group()
for i in range(3):
    asteroid = Enemy("asteroid.png", randint(0,650), 0,90,60,randint(1,5),randint(1,5))
    asteroids.add(asteroid)
game = 1

level_boss = 0
boss= Enemy('boss.png',30,40,80,100,5,5)


num_fire = 0
rel_time = False
while game:
    wn.blit(fon,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = 0
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <= 6 and rel_time == False:
                    rocket.fire()
                    num_fire +=1
                    
                elif num_fire >= 6 and rel_time == False:
                    rel_time = True
                    rel_timer = timer()
    
                        
    
    if not finish:
        label_lose= font1.render(f"Пропущено {lose}",True,(193,17,11))
        label_catch= font1.render(f"Збито {catch}",True,(13,197,11))
        rocket.show()
        rocket.move()
        monsters.draw(wn)
        monsters.update()
        asteroids.draw(wn)
        asteroids.update()
        bullets.draw(wn)
        bullets.update()
        wn.blit(label_catch,(10,10))
        wn.blit(label_lose,(10,45))
        
        colides = sprite.groupcollide(monsters,bullets,True,True)
        for c in colides:
            catch +=1
            enemy = Enemy("ufo.png", randint(0,650), 0,90,60,randint(1,5),randint(1,5))
            monsters.add(enemy)

            
        colides_a = sprite.groupcollide(asteroids,bullets,True,True)
        for c in colides_a:
            catch +=1
            asteroid = Enemy("asteroid.png", randint(0,650), 0,90,60,randint(1,5),randint(1,5))
            asteroids.add(asteroid)

        if catch >= 1 :
            finish = True
            level_boss = True
            
        if rel_time:
            if timer() - rel_timer > 3:
                rel_time = False
                num_fire = 0  
            time_to_fire =int(timer() - rel_timer +3 )
            label_rel = font1.render(f"Почекай ще {time_to_fire} ",True,(13,197,111))
            wn.blit(label_rel,(310,15)) 
    elif level_boss:
            label_boss_live = font1.render(f"Життя боcса: {boss.life}",True,(13,197,111))
            wn.blit(label_boss_live,(10,10))
            label_live = font1.render(f"Життя: {rocket.life}",True,(13,197,111))
            wn.blit(label_live,(10,50))
            rocket.move()
            rocket.show()
            bullets.draw(wn)
            bullets.update()
            boss.show()
            boss.rect.x += boss.speed
            if boss.rect.x < 0 or boss.rect.x > 600:
                boss.speed *= -1
                
            if sprite.spritecollide(boss,bullets,True):
                boss.life -=1
                
            if rel_time:
                if timer() - rel_timer > 3:
                    rel_time = False
                    num_fire = 0  
                time_to_fire =3 - int(timer() - rel_timer )
                label_rel = font1.render(f"Почекай ще {time_to_fire} ",True,(13,197,111))
                wn.blit(label_rel,(310,15)) 
                    
    if boss.life <= 0:
        level_boss = False
        label_lose= font2.render("ПеРЕмОгА",True,(13,197,11))
        wn.blit(label_lose,(190,200))
        boss.life = 0
        level_boss = False
        
    if lose >= 10 or sprite.spritecollide(rocket,monsters,False):
        finish = True
        label_lose= font2.render("Кінець гри!",True,(193,17,11))
        wn.blit(fon,(0,0))
        wn.blit(label_lose,(190,200))
        finish = True
        
    display.update()
    clock.tick(fps)