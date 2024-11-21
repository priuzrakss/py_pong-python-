import pygame
from peremennyie import screen_height, screen_width
from Ball import Ball

paddle_group = pygame.sprite.Group()

ball = Ball('Ball.png',screen_width/2,screen_height/2,4,4,paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)