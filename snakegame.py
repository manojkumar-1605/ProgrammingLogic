import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Snake characteristics
snake_block = 10
snake_speed = 15

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Function to display score
def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

# Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Function for the game
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    snake_list = []
    length_of_snake = 1

    # Random position for the apple
    apple_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    apple_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Initial positions for the snake
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    while not game_over:

        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake is within the boundaries
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [apple_x, apple_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # If the snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Set the speed of the snake
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
