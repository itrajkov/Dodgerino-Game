import pygame

class Meteor:
	
	speed = 10
	
	def __init__(self, x, screen):
		self.screen = screen
		self.x = x
		self.y = 50
		self.meteor_image = pygame.image.load('images/meteor.png')
		self.screen.blit(self.meteor_image, (self.x, self.y))

	def draw(self):
		self.screen.blit(self.meteor_image, (self.x, self.y))
		self.y += self.speed
		
	def is_offscreen(self, screen_size):
		return self.y > screen_size + 100
		
	# ACCESSORS!
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
	
	# Getter for the speed
	def get_speed(self):
		return self.speed