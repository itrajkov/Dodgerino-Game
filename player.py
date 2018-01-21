import glob
import pygame
import time

class Player():
	def __init__(self, screen_width, screen_height):
		
		# Player Position
		self.x = (screen_width / 2.30)
		self.y = (screen_height / 1.2)

		# Player Animation
		self.ani = glob.glob('images/player_animation/frame*')
		self.ani.sort()
		self.ani_frame = 0
		self.ani_len = len(self.ani)
		self.update_frame = 0

		# Player sounds
		self.player_score_sound = pygame.mixer.Sound("sound/player_score.wav")
		self.player_crash_sound = pygame.mixer.Sound("sound/player_crash.wav")
		
		# Player attributes
		self.score = 0
		self.name = "Unknown"
		
	def update(self):
		"Update the sprite of the player."
		if self.update_frame % 10 == 0:
			
			if self.ani_frame >= self.ani_len - 1:
				self.ani_frame = 0
				
			else:
				self.ani_frame += 1
		
			self.img = pygame.image.load(self.ani[self.ani_frame])
			self.deltaTime = 0
		self.update_frame += 1

	def draw(self, screen):
		"Draw the player to the screen."
		
		self.img = pygame.image.load(self.ani[self.ani_frame])
		self.update()
		screen.blit(self.img, (self.x, self.y))
		
	def crash(self):
		pygame.mixer.Sound.play(self.player_crash_sound)
	
	def add_score_point(self):
		"Gives the player a score point"
		self.score += 1
		pygame.mixer.Sound.play(self.player_score_sound)
	
	# ACCESSORS!!
	# Accessors for x position
	def getX(self):
		"Returns the x position of the player."
		return self.x

	def setX(self, x):
		"Sets the x position of the player."
		self.x = x
	
	# Accessors for y position
	def getY(self):
		"Returns the y position of the player."
		return self.y

	def setY(self, y):
		"Sets the y position of the player."
		self.y = y
		
	# Accessors for the score
	def get_score(self):
		return self.score
	
	def set_score(self, score):
		self.score = score
		
	# Accessors for the name
	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name