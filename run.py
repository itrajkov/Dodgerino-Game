"""
 The main file to run the game.
"""

import pygame
import random
import sqlite3
import time

from player import Player
from meteor import Meteor
from background import Background

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Get name from the player
player_name = input("Enter your name: ")

pygame.init()

# Set the width and height of the screen [width, height]
width = 800
height = 800
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Dodgerino Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Function to create a random pair of meteors
def create_random_pair():
	'''Creates a pair (x1, x2) that has two random Xs'''
	temp_list = [(width / 2.30), (width / 2.30) - 250 , (width / 2.30) + 250]
	x1 = random.choice(temp_list)
	temp_list = [x for x in temp_list if x != x1]
	x2 = random.choice(temp_list)
	return (x1, x2)

# Function to detect collision
def collision(x, y, x1, y1):
	return x == x1 and y1 >= y

# Instantiate objects
background =  Background(screen)
player = Player(width, height)
pair = create_random_pair()
meteor1 = Meteor(pair[0], screen)
meteor2 = Meteor(pair[1], screen)

# Set the player name
player.set_name(player_name)

# Start the background music
#background.start_background_music()

# Show the start screen
background.start_screen()

# -------- Main Program Loop -----------
if background.is_start_game():
	while not done:
		# --- Main event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
					#PLAYER !!
					if event.key == pygame.K_q:  # Goes Left
						player.setX(width / 2.30 - 250)
					elif event.key == pygame.K_w:  # Goes Middle
						player.setX(width / 2.30)
					elif event.key == pygame.K_e:  # Goes Right
						player.setX (width / 2.30 + 250)

		# --- Game logic should go here

		#Collision detection
		if collision(player.getX(), player.getY(), meteor1.getX(), meteor1.getY()) or collision(player.getX(), player.getY(), meteor2.getX(), meteor2.getY()):
			player.crash()
			background.end_screen(player.get_score())
			
			# Add info to database
			conn = sqlite3.connect("highscores.db")
			c = conn.cursor()
			c.execute("CREATE TABLE IF NOT EXISTS scores(name TEXT,score INTEGER)")
			c.execute("INSERT INTO scores (name,score) VALUES (?,?)", (player.get_name(), player.get_score()))
			# Save (commit) the changes
			conn.commit()
			conn.close()
			
			# Check if the player wants to play again
			done = not background.is_start_game()
			
			# Reset the game
			player.set_score(0)
			Meteor.speed = 10
			pair = create_random_pair()
			meteor1 = Meteor(pair[0], screen)
			meteor2 = Meteor(pair[1], screen)

		if(meteor1.is_offscreen(width)):
			pair = create_random_pair()
			meteor1 = Meteor(pair[0], screen)
			meteor2 = Meteor(pair[1], screen)
			Meteor.speed += 1
			player.add_score_point()


		# --- Screen-clearing code
		background.show_background_image()

		# --- Drawing code
		player.draw(screen)
		meteor1.draw()
		meteor2.draw()
		background.print_message("Score: " + str(player.get_score()), 0, 0)

		# --- Update the screen with what we've drawn.
		pygame.display.flip()

		# --- Limit to 60 frames per second
		clock.tick(60)

# Close the window and quit.
pygame.quit()
