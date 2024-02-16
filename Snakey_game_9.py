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
food = (0,225,0)

# Fonts for the game
pause_font_size = int(length/18)
exit_font_size = int(length/12)
score_font = pygame.font.Font("CHILLER.TTF", 30)
exit_font = pygame.font.Font("CHILLER.TTF", exit_font_size)
pause_font = pygame.font.Font("impact.ttf", pause_font_size)

# Sets the speed for the snake
clock = pygame.time.Clock()

# Create snake - replaces the previous snake drawing section in main loop
def draw_snake(snake_list):
    print(f"Snake list: {snake_list}") # For testing purposes
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])

# Function to display messages
def message(msg, txt_colour, bkgd_colour, msg_font):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(length/2, height/2))
    screen.blit(txt, text_box)

def game_loop():
    quit_game = False
    game_over = False

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
    snake_list = []
    snake_length = 1

    # Setting a random position for food
    food_x = round(random.randrange(20, length - 20) / 20) * 20
    food_y = round(random.randrange(20, height - 20) / 20) * 20

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            screen.fill(black)
            message("Press 'Q' to Quit or 'A' to play Again", red,
                    black, exit_font)
            pygame.display.update()

            # Check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop() # Restarts the main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit, SPACE to resume, R to reset"
                message(instructions, white, green, pause_font)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If user pressed X button, game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True

                        # If user presses 'R' button again, game is reset
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                        # If user presses the space-bar, game continues
                            if event.key == pygame.K_SPACE:
                                end = True

                        # If user presses 'Q' game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True

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
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        # Create rectangle for food
        pygame.draw.rect(screen, food, [food_x, food_y, 20, 20])
        pygame.display.update()

        # Create snake (replaces simple rectangle)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        pygame.display.update()

        # Collision dectection with food
        if snake_x == food_x and snake_y == food_y:
            # Set new random position for food if snake touches it
            food_x = round(random.randrange(20, length - 20) / 20) * 20
            food_y = round(random.randrange(20, height - 20) / 20) * 20

            # Increases snake length
            snake_length += 1

        # Sets the speed at which the interaction loop runs
        clock.tick(5)

    pygame.quit()
    quit()


# Main routine
game_loop()
