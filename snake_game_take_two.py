import pygame

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

    # Check if the game is over
    if snake_x < 0 or snake_x > window_x or snake_y < 0 or snake_x > window_y:
        # Display the game over screen
        font = pygame.font.Font(None, 36)
        game_over_text = font.render('Game Over!', True, red)
        window.blit(game_over_text, (350, 300))
        pygame.display.update()
        running = False

    # Draw the snake
    pygame.draw.rect(window, green, (snake_x, snake_y, snake_width, snake_height))

    # Draw the food
    pygame.draw.rect(window, red, (200, 200, 25, 25))



    # Update the display
    pygame.display.update()

# Quit the game engine
pygame.quit()
