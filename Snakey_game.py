import pygame
import random
import time
pygame.init()

height = random.randrange(200, 900, 20)
length = random.randrange(200, 1500, 20)
screen = pygame.display.set_mode((length, height))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - By Michael W", "sanke")

# Tuples containing the colours for the game
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# Fonts for the game
score_font = pygame.font.Font("CHILLER.TTF", 30)
exit_font = pygame.font.Font("impact.ttf", 60)

quit_game = False

# Snake is 20x20 start position is center of screen
snake_x = (length-20)/2
snake_y = (height-20)/2


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    
    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

pygame.quit()
quit()
