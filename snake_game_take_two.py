import pygame
import random

# Initialize the game engine
pygame.init()

# Set up the game window
window_x = 800
window_y = 600
window_size = (window_x, window_y)
window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define the initial position of the snake.
snake_x = window.get_width() // 2 - 25
snake_y = window.get_height() // 2 - 25

# Define the size of the snake.
snake_width = 50
snake_height = 50

# Define the speed of the snake
snake_speed = 5

# Define the colour of the snake
food_width = 50
food_height = 50

# Generate a random position for the food
food_x = random.randint(0, window.get_width() - food_width)
food_y = random.randint(0, window.get_height() - food_height)

# Keep track of the segments of the snake's body
snake_body = []

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    window.fill(black) # background colour
    
    # Get the state of all the currently pressed keys
    keys = pygame.key.get_pressed()

    # Handle users input
    if keys[pygame.K_UP]:
        # Move the snake up
        snake_y -= snake_speed
    elif keys[pygame.K_DOWN]:
        # Move the snake down
        snake_y += snake_speed
    elif keys[pygame.K_LEFT]:
        # Move the snake left
        snake_x -= snake_speed
    elif keys[pygame.K_RIGHT]:
        # Move the snake right
        snake_x += snake_speed

    # Update the game state
    # Add the current position of the snake's head to the snake_body list
    snake_body.append((snake_x, snake_y))

    # Check if the snake's head collides with the food
    if (snake_x < food_x + food_width and snake_x + snake_width > food_x 
    and snake_y < food_y + food_height and snake_y + snake_height > food_y):
        # Generate a new piece of food in a random location
        food_x = random.randint(0, window.get_width() - food_width)
        food_y = random.randint(0, window.get_height() - food_height)
    else:
        # Remove the tail of the snake if it hasn't eaten food.
        snake_body.pop(0)

    # Check if the game is over:
    # - Check if the sanke's head has collied with the wall.
    if snake_x < 0 or snake_x > window_x or snake_y < 0 or snake_x > window_y:
        # Display the game over screen
        font = pygame.font.Font(None, 36)
        game_over_text = font.render('Game Over!', True, red)
        window.blit(game_over_text, (350, 300))
        pygame.display.update()
        running = False
    
    # - Check if the snake's head has collied with any body part
    for x,y in snake_body[:-1]:
        if x == snake_x and y == snake_y:
            running = False

    # Draw the snake
    pygame.draw.rect(window, green, (snake_x, snake_y, snake_width, snake_height))

    # Draw the food
    pygame.draw.rect(window, red, (200, 200, 25, 25))



    # Update the display
    pygame.display.update()

# Quit the game engine
pygame.quit()
