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
yellow = (255,255,0)
maroon = (128,0,0)
purple = (128,0,128)

# Fonts for the game
pause_font_size = int(length/18)
exit_font_size = int(length/12)
score_font = pygame.font.Font("CHILLER.TTF", 50)
exit_font = pygame.font.Font("CHILLER.TTF", exit_font_size)
pause_font = pygame.font.Font("impact.ttf", pause_font_size)

# Sets the speed for the snake
clock = pygame.time.Clock()

# Function to keep track of the highest score - writes value to a file
def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value

# Function to update record of the highest score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score

# Save updated high score if player beats it
def save_high_score(high_score):
    high_score_file = open("HI_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()

# Display player score throughout the game
def player_score(score, score_colour, hi_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (5, 0)) # Coordinates for top left
    # High score
    display_score = score_font.render(f"High Score: {hi_score}", True,
                                      score_colour)
    screen.blit(display_score, (5, 40)) # Coordinates for top left lower down


# Create snake - replaces the previous snake drawing section in main loop
def draw_snake(snake_list):
    pygame.draw.rect(screen, yellow, [snake_list[0][0], snake_list[0][1],
                                      20, 20])
    for i in snake_list[1:]:
        pygame.draw.rect(screen, maroon, [i[0], i[1], 20, 20])

# Function to display messages
def message(msg, txt_colour, bkgd_colour, msg_font):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(length/2, height/2))
    screen.blit(txt, text_box)

def snake_direction_check(s_dir, new_dir):
    if s_dir == "left" and new_dir == "right" or s_dir == "right" and\
        new_dir == "left" or s_dir == "up" and new_dir == \
        "down" or s_dir == "down" and new_dir == "up":
        return s_dir
    else:
        return new_dir

def game_loop():
    start_time = time.time() # To record score (time) form start of game
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
    snake_dir = ""

    # Setting a random position for food
    food_x = round(random.randrange(20, length - 20) / 20) * 20
    food_y = round(random.randrange(20, height - 20) / 20) * 20

    # Load the high score
    high_score = load_high_score()

    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            save_high_score(high_score)
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
                    if snake_dir == "right":
                        pass
                    else:
                        snake_x_change = -20
                        snake_y_change = 0
                        snake_dir = "left"
                if event.key == pygame.K_RIGHT:
                    if snake_dir == "left":
                        pass
                    else:
                        snake_x_change = 20
                        snake_y_change = 0
                        snake_dir = "right"
                if event.key == pygame.K_UP:
                    if snake_dir == "down":
                        pass
                    else:
                        snake_x_change = 0
                        snake_y_change = -20
                        snake_dir = "up"
                if event.key == pygame.K_DOWN:
                    if snake_dir == "up":
                        pass
                    else:
                        snake_x_change = 0
                        snake_y_change = 20
                        snake_dir = "down"

        if snake_x >= length or snake_x < 0 or snake_y >= height or snake_y \
                < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        # Using a sprite to represent food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        # Create snake (replaces simple rectangle)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Keeping track of the player's score
        score = snake_length - 1
        player_score(score, purple, high_score)

        pygame.display.update()

        # Get high score
        high_score = update_high_score(score, high_score)

        # Link speed of snake to player score in increase difficulty
        if score > 10:
            speed = score
        else:
            speed = 10

        # Collision dectection with food
        if snake_x == food_x and snake_y == food_y:
            # Set new random position for food if snake touches it
            food_x = round(random.randrange(20, length - 20) / 20) * 20
            food_y = round(random.randrange(20, height - 20) / 20) * 20

            # Increases snake length
            snake_length += 1

        # Sets the speed at which the interaction loop runs
        clock.tick(speed)


    pygame.quit()
    quit()


# Main routine
game_loop()
