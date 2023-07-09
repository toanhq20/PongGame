import pygame
from pygame.locals import *

# init
pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# define colors
bg = (50, 25, 50)

def draw_board():
    screen.fill(bg)

run = True
while run:
    draw_board()
    for event in pygame.event.get():  # all events
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()
