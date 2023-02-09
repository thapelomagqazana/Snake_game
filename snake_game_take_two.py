import pygame
import random
import sys

# Initialize game
pygame.init()

# Set up display
win = pygame.display.set_mode((500,500))

# Initialize the snake's starting position and size.
snake_x = 250
snake_y = 250
snake_size = 20

# Generate the first food items at a random location.
food_x = random.randint(0, 480)
food_y = random.randint(0, 480)
food_size = 20

running = True

def update_game_state():
    global running, snake_x, snake_y
    # Move the snake to its new position
    snake_x += snake_size
    snake_y += snake_size
    
    # Check if the snake has collided with the walls or itself
    if snake_x >= 500 or snake_y >= 500 or snake_x < 0 or snake_y < 0:
        running = False
    
    # Check if the snake has eaten the food item
    if snake_x == food_x and snake_y == food_y:
        # Generate a new food item at a random location
        food_x = random.randint(0, 480)
        food_y = random.randint(0, 480)

def render_game():
    # Clear the display
    win.fill((255,255,255))
    
    # Draw the walls
    wall_colour = (0,0,0)
    wall_width = 20
    wall_height = 500
    
    pygame.draw.rect(win,wall_colour, (0, 0, wall_width, wall_height))
    pygame.draw.rect(win, wall_colour, (480, 0, wall_width, wall_height))
    pygame.draw.rect(win, wall_colour, (0, 0, 500, wall_width))
    pygame.draw.rect(win, wall_colour, (0, 480, 500, wall_width))
    
    # Draw the snake
    pygame.draw.rect(win, (0,0,0), (snake_x, snake_y, snake_size, snake_size))
    
    # Draw the food item
    pygame.draw.rect(win, (255, 0, 0), (food_x, food_y, food_size, food_size))
    
    # Update the display
    pygame.display.update()
    

def gameLoop():
    # Run the game loop
    global running, snake_x, snake_y
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
        # Check fo player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Move the snake up
            snake_y -= snake_size
        elif keys[pygame.K_DOWN]:
            # Move the snake down
            snake_y += snake_size
        elif keys[pygame.K_LEFT]:
            # Move the snake left
            snake_x -= snake_size
        elif keys[pygame.K_RIGHT]:
            # Move the snake right
            snake_x += snake_size
            
        # # End the game if the player quits
        # if event.type == pygame.QUIT:
        #     running = False
            
            
        # Update the game state
        update_game_state()
        
        # Render the game
        render_game()
        

    # Quit the game
    pygame.quit()
    
    # Close the display window
    sys.exit()
    

if __name__ == '__main__':
    gameLoop()