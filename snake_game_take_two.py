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

# Create a snake
snake_size = 20
snake_list = []
for i in range(3):
    x = 100 - i * snake_size
    y = 100
    segment = pygame.Rect(x ,y ,snake_size, snake_size)
    snake_list.append(segment)

# Place the food
food_size = 20
food = pygame.Rect(random.randint(0, window_x-food_size), 
random.randint(0, window_y-food_size), food_size, food_size)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Initialize the direction and speed of the snake.
direction = 'right'
snake_speed = 5

# # Define the size of the snake.
# snake_width = 50
# snake_height = 50

# # Define the speed of the snake
# snake_speed = 5

# # Define the colour of the snake
# food_width = 50
# food_height = 50

# # Generate a random position for the food
# food_x = random.randint(0, window.get_width() - food_width)
# food_y = random.randint(0, window.get_height() - food_height)

# # Keep track of the segments of the snake's body
# snake_body = []

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#     # Clear the screen
#     window.fill(black) # background colour

    # Handle user's input
    # Get the state of all the currently pressed keys
    keys = pygame.key.get_pressed()

    # Check if the up arrow key is pressed
    if keys[pygame.K_UP] and direction != 'down':
        direction = 'up'
    
    # Check if the down arrow key is pressed
    elif keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'

    # Check if the right arrow key is pressed
    elif keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    
    # Check if the left arrow key is pressed
    elif keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'

    # Move the snake to its current position
    for i in range(len(snake_list)-1,0,-1):
        snake_list[i].x = snake_list[i-1].x
        snake_list[i].y = snake_list[i-1].y
    
    if direction == 'right':
        snake_list[0].x += snake_speed
    elif direction == 'left':
        snake_list[0].x -= snake_speed
    elif direction == 'up':
        snake_list[0].y -= snake_speed
    elif direction == 'down':
        snake_list[0].y += snake_speed

    # Check for collisions with the wall
    if (snake_list[0].x < 0 or snake_list[0].x > window_x - snake_size 
    or snake_list[0].y < 0 or snake_list[0].y > window_y - snake_size):
        running = False
    
    # Check for collisions with the snake's own body
    for i in range(1, len(snake_list)):
        if snake_list[0].colliderect(snake_list):
            running = False
            
    # Draw the snake
    for segment in snake_list:
        pygame.draw.rect(window, green, segment)

    # Draw the food
    pygame.draw.rect(window, red, food)



    # Update the display
    pygame.display.update()

# Quit the game engine
pygame.quit()
