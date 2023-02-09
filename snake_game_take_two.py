import pygame

# Initialize the game engine
pygame.init()

# Set up the game window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    window.fill(black) # background colour
    
    # Handle users input
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP]:
    #     # Move the snake up
    # elif keys[pygame.K_DOWN]:
    #     # Move the snake down
    # elif keys[pygame.K_LEFT]:
    #     # Move the snake left
    # elif keys[pygame.K_RIGHT]:
    #     # Move the snake right

    # Draw the snake
    pygame.draw.rect(window, (0, 255, 0), (100, 100, 50, 50))

    # Draw the food
    pygame.draw.rect(window, (255, 0, 0), (200, 200, 25, 25))

    # Update the display
    pygame.display.update()

# Quit the game engine
pygame.quit()
