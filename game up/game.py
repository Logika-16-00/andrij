#import libraries
from pygame import *
from random import *
import os

#initialise pygame

mixer.init()
init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create game window
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('Jumpy')

#set frame rate
clock = time.Clock()
FPS = 60



#load music and sounds
mixer.music.load('music/music.mp3')
mixer.music.set_volume(0.6)
mixer.music.play(-1, 0.0)
jump_fx = mixer.Sound('music/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = mixer.Sound('music/death.mp3')
death_fx.set_volume(0.5)

#game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

#game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
current_state = MENU

if os.path.exists('score.txt'):
	with open('score.txt', 'r') as file:
		high_score = int(file.read())
else:
	high_score = 0

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL = (153, 217, 234)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#define font
font_small = font.SysFont('Lucida Sans', 20)
font_big = font.SysFont('Lucida Sans', 24)
font_title = font.SysFont('Lucida Sans', 40)

#load images
jumpy_image = image.load('img/Player.png').convert_alpha()
bg_image = transform.scale(image.load("img/fon.png"), (700,600 ))
platform_image = image.load('img/Platform.webp').convert_alpha()
menu_bg = transform.scale(image.load("img/fon.png"), (700,600 ))
menu_blockback = transform.scale(image.load("img/BlockBackground.png"), (100,100 ))

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#function for drawing info panel
def draw_panel():
	draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
	draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
	draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

#function for drawing the background
def draw_bg(bg_scroll):
	screen.blit(bg_image, (0, 0 + bg_scroll))
	screen.blit(bg_image, (0, -600 + bg_scroll))

#button class
class Button:
	def __init__(self, x, y, width, height, text, color, hover_color):
		self.rect = Rect(x, y, width, height)
		self.text = text
		self.color = color
		self.hover_color = hover_color
		self.current_color = color
		
	def draw(self):
		mouse_pos = mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.current_color = self.hover_color
		else:
			self.current_color = self.color
			
		draw.rect(screen, self.current_color, self.rect)
		draw.rect(screen, BLACK, self.rect, 2)
		text_surf = font_big.render(self.text, True, BLACK)
		text_rect = text_surf.get_rect(center=self.rect.center)
		screen.blit(text_surf, text_rect)
		
	def is_clicked(self, pos):
		return self.rect.collidepoint(pos)

#player class
class Player(sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = transform.scale(jumpy_image, (45, 45))
		self.width = 25
		self.height = 40
		self.rect = Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)
		self.vel_y = 0
		self.flip = False

	def move(self):
		#reset variables
		scroll = 0
		dx = 0
		dy = 0

		#process keypresses
		keys = key.get_pressed()
		if keys[K_a]:
			dx = -10
			self.flip = True
		if keys[K_d]:
			dx = 10
			self.flip = False

		#gravity
		self.vel_y += GRAVITY
		dy += self.vel_y

		#ensure player doesn't go off the edge of the screen
		if self.rect.left + dx < 0:
			dx = -self.rect.left
		if self.rect.right + dx > SCREEN_WIDTH:
			dx = SCREEN_WIDTH - self.rect.right

		#check collision with platforms
		for platform in platform_group:
			#collision in the y direction
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if above the platform
				if self.rect.bottom < platform.rect.centery:
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
						dy = 0
						self.vel_y = -20
						jump_fx.play()

		#check if the player has bounced to the top of the screen
		if self.rect.top <= SCROLL_THRESH:
			#if player is jumping
			if self.vel_y < 0:
				scroll = -dy

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy + scroll

		#update mask
		self.mask = mask.from_surface(self.image)

		return scroll

	def show(self):
		screen.blit(transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))

#platform class
class Platform(sprite.Sprite):
	def __init__(self, x, y, width, moving):
		super().__init__()
		self.image = transform.scale(platform_image, (width, 60))
		self.moving = moving
		self.move_counter = randint(0, 50)
		self.direction = choice([-1, 1])
		self.speed = randint(1, 2)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, scroll):
		#moving platform side to side if it is a moving platform
		if self.moving == True:
			self.move_counter += 1
			self.rect.x += self.direction * self.speed

		#change platform direction if it has moved fully or hit a wall
		if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
			self.direction *= -1
			self.move_counter = 0

		#update platform's vertical position
		self.rect.y += scroll

		#check if platform has gone off the screen
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

#create buttons
start_button = Button(SCREEN_WIDTH//2 - 100, 250, 200, 50, "START GAME", GREEN, (100, 255, 100))
quit_button = Button(SCREEN_WIDTH//2 - 100, 320, 200, 50, "QUIT", RED, (255, 100, 100))
restart_button = Button(SCREEN_WIDTH//2 - 100, 350, 200, 50, "PLAY AGAIN", GREEN, (100, 255, 100))
menu_button = Button(SCREEN_WIDTH//2 - 100, 420, 200, 50, "MAIN MENU", BLUE, (100, 100, 255))

#player instance
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#create sprite groups
platform_group = sprite.Group()
enemy_group = sprite.Group()

#create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)

def reset_game():
	global score, scroll, fade_counter, game_over
	game_over = False
	score = 0
	scroll = 0
	fade_counter = 0
	#reposition jumpy
	jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
	#reset enemies
	enemy_group.empty()
	#reset platforms
	platform_group.empty()
	#create starting platform
	platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
	platform_group.add(platform)

#game loop
run = True
while run:

	clock.tick(FPS)

	if current_state == MENU:
		screen.blit(menu_bg, (-50, 0))
		screen.blit(menu_blockback, (0, 500))
		screen.blit(menu_blockback, (50, 500))
		screen.blit(menu_blockback, (100, 500))
		screen.blit(menu_blockback, (150, 500))
		screen.blit(menu_blockback, (200, 500))
		screen.blit(menu_blockback, (250, 500))
		screen.blit(menu_blockback, (300, 500))
		draw_text('JUMPY GAME', font_title, WHITE, SCREEN_WIDTH//2 - 120, 150)
		
		start_button.draw()
		quit_button.draw()
		
		for e in event.get():
			if e.type == QUIT:
				run = False
			if e.type == MOUSEBUTTONDOWN:
				if start_button.is_clicked(e.pos):
					current_state = PLAYING
					reset_game()
				if quit_button.is_clicked(e.pos):
					run = False
					
	elif current_state == PLAYING:
		if game_over == False:
			scroll = jumpy.move()

			#draw background
			bg_scroll += scroll
			if bg_scroll >= 600:
				bg_scroll = 0
			draw_bg(bg_scroll)

			#generate platforms
			if len(platform_group) < MAX_PLATFORMS:
				p_w = randint(40, 60)
				p_x = randint(0, SCREEN_WIDTH - p_w)
				p_y = platform.rect.y - randint(80, 120)
				p_type = randint(1, 2)
				if p_type == 1 and score > 500:
					p_moving = True
				else:
					p_moving = False
				platform = Platform(p_x, p_y, p_w, p_moving)
				platform_group.add(platform)

			#update platforms
			platform_group.update(scroll)

			#update score
			if scroll > 0:
				score += scroll

			#draw line at previous high score
			draw.line(screen, WHITE, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
			draw_text('HIGH SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

			#draw sprites
			platform_group.draw(screen)
			enemy_group.draw(screen)
			jumpy.show()

			#draw panel
			draw_panel()

			#check game over
			if jumpy.rect.top > SCREEN_HEIGHT:
				game_over = True
				current_state = GAME_OVER
				death_fx.play()
				
		else:
			current_state = GAME_OVER
			death_fx.play()
			
	elif current_state == GAME_OVER:
		if fade_counter < SCREEN_WIDTH:
			fade_counter += 5
			for y in range(0, 6, 2):
				draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
				draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
		else:
			screen.fill(BLACK)
			draw_text('GAME OVER!', font_big, WHITE, 130, 200)
			draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
			
			
			#update high score
			if score > high_score:
				high_score = score
				with open('score.txt', 'w') as file:
					file.write(str(high_score))
			
			restart_button.draw()
			menu_button.draw()
			
			for e in event.get():
				if e.type == QUIT:
					run = False
				if e.type == MOUSEBUTTONDOWN:
					if restart_button.is_clicked(e.pos):
						current_state = PLAYING
						reset_game()
					if menu_button.is_clicked(e.pos):
						current_state = MENU

	#event handler for quitting
	for e in event.get():
		if e.type == QUIT:
			#update high score
			if score > high_score:
				high_score = score
				with open('score.txt', 'w') as file:
					file.write(str(high_score))
			run = False

	#update display window
	display.update()

quit()