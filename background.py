import pygame

class Background():
	
	def __init__(self, screen):
		self.screen = screen
		self.background_image = pygame.image.load('images/background.png')
		self.start_screen_image = pygame.image.load('images/startscreen.png')
		self.background_sound = pygame.mixer.music.load("sound/bgmusic.wav")
		
	def start_background_music(self):
		pygame.mixer.music.play(-1)
		
	def show_background_image(self):
		self.screen.blit(self.background_image, (0, 0))
		
	def print_message(self, message, x_position, y_position):
		font = pygame.font.Font(None, 40)
		text = font.render(message, 1, (255,0,0))
		self.screen.blit(text, (x_position,y_position))
		
	def start_screen(self):
		self.screen.blit(self.start_screen_image, (0, 0))
		self.print_message("Press \"Space\" to start the game!", (800/3.7), (800/2))
		pygame.display.flip()
		
	def end_screen(self, player_score):
		self.screen.blit(self.start_screen_image, (0, 0))
		self.print_message("Press \"Space\" to restart the game!", (800/3.7), (800/2))
		self.print_message("Score: " + str(player_score), 0, 0)
		pygame.display.flip()
		
	def is_start_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					return True
	