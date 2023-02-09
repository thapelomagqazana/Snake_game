import pygame

# Initialize the game engine
pygame.init()

# Set up the game window
window_size = (400, 400)
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
    window.fill(black)
    
    # Update the display
    pygame.display.update()

# Quit the game engine
pygame.quit()
