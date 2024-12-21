from pygame import *

#  створюємо вікно
wn  = display.set_mode((600,600))
display.set_caption("Лабіринт")
#фон 
fon = transform.scale(image.load("background.jpg"),(600,600))

clock = time.Clock()
FPS= 120
game = 1


mixer.init()
#фонова музика
mixer.music.load("jungles.ogg")
mixer.music.play()
#музика для зіткення
money= mixer.Sound("money.ogg")
kick = mixer.Sound('kick.ogg')

font.init()
font1 = font.Font(None,70)
font2 = font.Font(None,20)
win = font1.render('You win',True,(23,231,43))
lose = font1.render('You lose',True,(250,87,9))



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
    
class Wall(sprite.Sprite):
    def __init__(self,color,x,y,size_x,size_y):
        super().__init__()
        self.color = color
        self.size_x =size_x
        self.size_y = size_y
        self.wall = Surface((self.size_x,self.size_y))
        self.wall.fill(self.color)
        #хіт бокс
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def wall_draw(self):
        wn.blit(self.wall,(self.rect.x,self.rect.y))
        


 

#створюємо стіни
color = (32,54,122)
wall1= Wall(color,0,0,600,10)
wall2= Wall(color,0,600-10,600,10)
wall3= Wall(color,0,0,10,600)
wall4=Wall(color,600-10,0,10,600)

wall5 = Wall(color,90,130,900,10)
wall6 = Wall(color,0,290,300,10)
wall7 = Wall(color,90,420,900,10)
hero = Player("hero.png",300,10,100,100,3,3)
enemy = Player("cyborg.png",450,300,100,100,3,1)
finish = Player("treasure.png",300,500,80,50,0,0)
dx = 3



while game:    
    
    #відображаємо фон
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    hero.show()
    hero.move()
    enemy.show()
    finish.show()
    enemy.rect.x += dx 
    if enemy.rect.x > 700 or enemy.rect.x < 100:
        dx *= -1
        
    
    wall1.wall_draw()
    wall2.wall_draw()
    wall3.wall_draw()
    wall4.wall_draw()
    wall5.wall_draw()
    wall6.wall_draw()
    wall7.wall_draw()

    

    if sprite.collide_rect(hero,enemy):
        kick.play()
        wn.blit(lose,(200,200))
        # game = 0
    
    

    if sprite.collide_rect(hero,finish):
        money.play()
        wn.blit(win,(200,200))
     




 





    clock.tick(FPS)
    display.update()