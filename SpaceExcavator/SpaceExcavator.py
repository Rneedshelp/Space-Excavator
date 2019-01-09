import sys
import pygame
from pygame import *
import random
import time
from time import sleep
from pygame import *
from os import path
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SPACE EXCAVATOR')
clock = pygame.time.Clock()

img_dir = path.join(path.dirname(__file__), 'images')
sound_path = path.join(path.dirname(__file__), 'sounds')
#Sounds
selectsound = pygame.mixer.Sound(path.join(sound_path, 'select.wav'))
#Images
space = pygame.image.load('/home/linuxstudent/SpaceExcavator/images/space.jpg')
menuscreen = pygame.image.load('/home/linuxstudent/SpaceExcavator/images/menuscreen.jpg')
menuscreen = pygame.transform.scale(menuscreen,(WIDTH,HEIGHT))
victoryscreen = pygame.image.load('/home/linuxstudent/SpaceExcavator/images/victorypage.jpg')
victoryscreen = pygame.transform.scale(victoryscreen,(WIDTH,HEIGHT))


#COLORS
RED = (255,0,0)
BRICK = (204,0,0)
SILVER = (227,225,255)
GREY = (128,128,128)
PURPLE = (153,0,153)
GREEN = (0,103,0)
LIGHTGREEN = (0,155,0)
BLACK = (0,0,1)
PINK = (255,0,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#Function for intro
def intro():
	for i in range(100):
		screen.fill(BLACK)
		fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',30)
		TextSurf, TextRect = text_objects('CPSC 386 Project 5 Video Game',fontsize,SILVER)
		TextRect.center = ((390),(i))
		screen.blit(TextSurf,TextRect)
		TextSurf, TextRect = text_objects('Richard Echeverria Presents:',fontsize,SILVER)
		TextRect.center = ((395),(i * 2))
		screen.blit(TextSurf,TextRect)
		pygame.display.flip()
	pygame.time.wait(5000)
	menu()
	
	
#Function for Main Menu
def menu():
	pygame.mixer.music.load("/home/linuxstudent/SpaceExcavator/sounds/menu.wav")
	pygame.mixer.music.play(-1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.blit(menuscreen,(0,0))
		fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',65)
		TextSurf, TextRect = text_objects('SPACE EXCAVATOR',fontsize,SILVER)
		TextRect.center = ((410),(60))
		screen.blit(TextSurf,TextRect)
		button("Start Game",145,303,100,55,GREEN,LIGHTGREEN,(140,300,110,60),game)
		button("Quit Game",555,303,100,55,BRICK,RED,(550,300,110,60),exitgame)
		button("Controls",360,450,100,55,PURPLE,PINK,(354,447,112,62),controls)
		
		pygame.display.flip()
		clock.tick(15)

#Function for buttons
def button(msg,x,y,w,h,normal,bright,panel,choice = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x + w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen,GREY,panel)			
		pygame.draw.rect(screen,bright,(x,y,w,h))
		if click[0] == 1 and choice != None:
			selectsound.play()
			sleep(1)
			choice()
	else:
		pygame.draw.rect(screen,GREY,panel)		
		pygame.draw.rect(screen,normal,(x,y,w,h))
		
	buttontext = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',13)
	TextSurf, TextRect = text_objects(msg,buttontext,BLACK)
	TextRect.center = ((x+(w/2)),(y+(h/2)))
	screen.blit(TextSurf, TextRect)

#Function to create font size,color, and render coordinates to return 
def text_objects(text,fontsize,color):
	textsurf = fontsize.render(text,True,color)
	return textsurf, textsurf.get_rect()

	
#Function that creates game over screen. Stops music and plays gameover sounds
def crashed():
	fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',100)
	TextSurf, TextRect = text_objects('GAME OVER',fontsize,RED)
	TextRect.center = (400,100)
	screen.blit(TextSurf,TextRect)
	pygame.mixer.music.stop()
	pygame.mixer.music.load("/home/linuxstudent/SpaceExcavator/sounds/gameover.wav")
	pygame.mixer.music.play(1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
	
		button("Play Again",145,303,100,55,GREEN,LIGHTGREEN,(140,300,110,60),game)
		button("Menu",555,303,100,55,BRICK,RED,(550,300,110,60),menu)

		pygame.display.flip()
		clock.tick(15)	

def winner():
	screen.blit(victoryscreen,(0,0))
	fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',70)
	TextSurf, TextRect = text_objects('CONGRATULATIONS',fontsize ,WHITE)
	TextRect.center = (400,70)
	screen.blit(TextSurf,TextRect)
	TextSurf, TextRect = text_objects('YOU WIN!!!',fontsize ,WHITE)
	TextRect.center = (400,135)
	screen.blit(TextSurf,TextRect)
	pygame.mixer.music.stop()
	pygame.mixer.music.load("/home/linuxstudent/SpaceExcavator/sounds/victory.wav")
	pygame.mixer.music.play(1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
	
		button("Play Again",145,303,100,55,GREEN,LIGHTGREEN,(140,300,110,60),game)
		button("Menu",555,303,100,55,BRICK,RED,(550,300,110,60),menu)

		pygame.display.flip()
		clock.tick(15)


#Function called to exit the program
def exitgame():
	sys.exit()


#Function that creates the page used for controls and how to play 
def controls():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.blit(menuscreen,(0,0))
		fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',75)
		TextSurf, TextRect = text_objects('HOW TO PLAY',fontsize,SILVER)
		TextRect.center = ((280),(60))
		screen.blit(TextSurf,TextRect)
		
		fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',17)
		TextSurf, TextRect = text_objects('-PRESS THE "RIGHT ARROW KEY" TO MOVE SHIP RIGHT',fontsize,WHITE)
		TextRect.center = ((280),(150))
		screen.blit(TextSurf,TextRect)
	
		TextSurf, TextRect = text_objects('-PRESS THE "LEFT ARROW KEY" TO MOVE SHIP LEFT',fontsize,WHITE)
		TextRect.center = ((270),(200))
		screen.blit(TextSurf,TextRect)
		
		TextSurf, TextRect = text_objects('-Press the "SPACEBAR" to shoot a bullet at the oncoming asteroids',fontsize,WHITE)
		TextRect.center = ((380),(250))
		screen.blit(TextSurf,TextRect)
		
		TextSurf, TextRect = text_objects('-Collect All 7 PowerStars to win the game!',fontsize,(255,255,255))
		TextRect.center = ((240),(300))
		screen.blit(TextSurf,TextRect)
		
		fontsize = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',13)
		TextSurf, TextRect = text_objects('-Asteroids will spawn either a kamikaze alien, a temporary gun powerup, or a powerstar',fontsize,WHITE)
		TextRect.center = ((380),(330))
		screen.blit(TextSurf,TextRect)

		button("Menu",360,450,100,55,PURPLE,PINK,(354,447,112,62),menu)
		pygame.display.flip()
		clock.tick(15)

#Main Game Function
def game():
 score = 0
 FPS = 60
 POWERUP_TIME = 5000
# initialize pygame and create window
 pygame.init()
 pygame.mixer.init()
 screen = pygame.display.set_mode((WIDTH, HEIGHT))
 pygame.display.set_caption("Space Excavator")
 clock = pygame.time.Clock()


# Load all game sounds
 shoot_sound = pygame.mixer.Sound(path.join(sound_path, 'pew.wav'))
 power_sound = pygame.mixer.Sound(path.join(sound_path, 'pow5.wav'))
 expl_sounds = []
 for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_path, sound)))
 player_die_sound = pygame.mixer.Sound(path.join(sound_path, 'crash.wav'))
 star_collect_sound = pygame.mixer.Sound(path.join(sound_path, 'starget.wav'))
 pygame.mixer.music.set_volume(1.0)
 pygame.mixer.music.load(path.join(sound_path, 'gameplay.wav'))
 #pygame.mixer.music.set_volume(0.10)

 pygame.mixer.music.play(1)




 font_name = pygame.font.match_font('arial')

 def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

 def obstacles(all_sprites,enemies):
    m = Pack()
    all_sprites.add(m)
    enemies.add(m)

 def draw_lives(surf, x, y, lives, img,stars, num,location):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
    for i in range(num):
    	location += (i + 20)
    	star_rect = stars.get_rect()
    	star_rect.x = x + 50
    	star_rect.y = y + location + (2*i)
    	surf.blit(stars,star_rect)
   

 class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (70, 60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.num = 0
        self.location = 55
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.shoot_delay = 450

    def update(self):
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot(all_sprites,bullets)
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 5
        self.power_time = pygame.time.get_ticks()

    def shoot(self,all_sprites,bullets):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

 class Pack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-80, -20)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -100 or self.rect.right > WIDTH + 100:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

 class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        if score >= 3000:
        	self.speedy = -50
        if score >= 1500:
        	self.speedy = -20
        else:	
        	self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

 class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['gun','alien','star'])
        
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top > HEIGHT:
            self.kill()

 class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Load all game graphics
 background = pygame.image.load(path.join(img_dir, "space.jpg")).convert()
 background_rect = background.get_rect()
 player_img = pygame.image.load(path.join(img_dir, "samus.png")).convert()
 powerstar = pygame.image.load(path.join(img_dir, "star.png")).convert()
 powerstar = pygame.transform.scale(powerstar,(25,25))
 player_mini_img = pygame.transform.scale(player_img, (30,30))
 player_mini_img.set_colorkey(BLACK)
 bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
 meteor_images = []
 meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
               'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png']
 for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
 explosion_anim = {}
 explosion_anim['lg'] = []
 explosion_anim['sm'] = []
 explosion_anim['player'] = []
 for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)
 powerup_images = {}
 powerup_images['alien'] = pygame.image.load(path.join(img_dir, 'alien.png')).convert()
 powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'boost.png')).convert()
 powerup_images['star'] = pygame.image.load(path.join(img_dir, 'star.png')).convert()


# Game loop
 game_over = True
 running = True
 while True:
     if game_over:
         
         game_over = False
         all_sprites = pygame.sprite.Group()
         enemies = pygame.sprite.Group()
         bullets = pygame.sprite.Group()
         powerups = pygame.sprite.Group()
         player = Player()
       	 all_sprites.add(player)
       	 for i in range(8):
       	       obstacles(all_sprites,enemies)

    # keep loop running at the right speed
     clock.tick(FPS)
    # Process input (events)
     for event in pygame.event.get():
        # check for closing window
       	 if event.type == pygame.QUIT:
		 sys.exit()

    # Update
     all_sprites.update()

    # check to see if a bullet hit a mob
     hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
     for hit in hits:
       	 score += 50 - hit.radius
       	 random.choice(expl_sounds).play()
       	 expl = Explosion(hit.rect.center, 'lg')
       	 all_sprites.add(expl)
       	 if random.random() > 0.8:
       	     pow = Pow(hit.rect.center)
       	     all_sprites.add(pow)
       	     powerups.add(pow)
       	 obstacles(all_sprites,enemies)

    # check to see if a mob hit the player
     hits = pygame.sprite.spritecollide(player, enemies, True,pygame.sprite.collide_mask)
     for hit in hits:
       	 expl = Explosion(hit.rect.center, 'sm')
       	 all_sprites.add(expl)
       	 obstacles(all_sprites,enemies)
       	 player_die_sound.play()
       	 death_explosion = Explosion(player.rect.center, 'player')
       	 all_sprites.add(death_explosion)
       	 player.hide()
       	 player.lives -= 1

    # check to see if player hit a powerup
     hits = pygame.sprite.spritecollide(player, powerups, True)
     for hit in hits:
	if hit.type == 'alien':
        	expl = Explosion(hit.rect.center, 'sm')
       	 	all_sprites.add(expl)
       	 	obstacles(all_sprites,enemies)
       	 	player_die_sound.play()
       	 	death_explosion = Explosion(player.rect.center, 'player')
       	 	all_sprites.add(death_explosion)
       	 	player.hide()
       	 	player.lives -= 1
	if hit.type == 'gun':
       		player.powerup()
       	     	power_sound.play()
       	if hit.type == 'star':
       		player.num += 1
       		star_collect_sound.play()
 
       		

    # if the player died and the explosion has finished playing
     if player.lives == 0 and not death_explosion.alive():
     	 crashed()
       	 game_over = True

    # Draw / render
     screen.fill(BLACK)
     screen.blit(background, background_rect)
     all_sprites.draw(screen)
     font = pygame.font.Font('/home/linuxstudent/SpaceExcavator/Fonts/space_invaders.ttf',15)
     text = font.render("Score: ",True,(255,255,255))
     screen.blit(text,(0,0))
     draw_text(screen, str(score), 20, 80,-2)
     draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img,powerstar,player.num,player.location)
     if player.num == 7:
       		winner()
    # *after* drawing everything, flip the display
     pygame.display.flip()


     
if __name__ == "__main__":
	intro()
