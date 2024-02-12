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
msg_font = pygame.font.Font("CHILLER.TTF", 230)

# Function to display messages
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(length/2, height/2))
    screen.blit(txt, text_box)

# Sets the speed for the snake
clock = pygame.time.Clock()

quit_game = False

# Snake is 20x20 start position is center of screen
snake_x = (length-20)/2
snake_y = (height-20)/2
# Make sure snake aligns correct in the grid
if (length/20) % 2 == 0:
    snake_x += 10
if (height/20) % 2 == 0:
    snake_y += 10

# Holds the value of x and y changes in the snake
snake_x_change = 0
snake_y_change = 0


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            if event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            if event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    if snake_x >= length or snake_x < 0 or snake_y >= height or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    # Sets the speed at which the interaction loop runs
    clock.tick(5)

message("YOU DIED!", red, black)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
