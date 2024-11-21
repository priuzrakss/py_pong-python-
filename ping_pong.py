import pygame
import sys

from Player import Player
from peremennyie import screen, screen_width, screen_height, bg_color, middle_strip, clock, accent_color
from Ball import Ball
from Opponent import Opponent
from Classes import GameManager
from SpriteGroups import paddle_group, ball_sprite

# Game objects
player = Player('Paddle.png', 20,screen_height/2,5)
opponent = Opponent('Paddle red.png',screen_width - 20,screen_width/2,5)

paddle_group.add(player)
paddle_group.add(opponent)

game_manager = GameManager(ball_sprite,paddle_group)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.movement -= player.speed
			if event.key == pygame.K_DOWN:
				player.movement += player.speed
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player.movement += player.speed
			if event.key == pygame.K_DOWN:
				player.movement -= player.speed
	
	# Background Stuff
	screen.fill(bg_color)
	pygame.draw.rect(screen,accent_color,middle_strip)
	
	# Run the game
	game_manager.run_game()

	# Rendering
	pygame.display.flip()
	clock.tick(120)