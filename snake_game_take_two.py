import turtle
import random
import time

# Set the game screen
screen = turtle.Screen()
# Give the screen a name
screen.title('Snake Game')
screen.setup(width=600, height=600)
# Background colour of the screen
screen.bgcolor('black')
screen.tracer(0)

# Create a turtle as a snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape('square')
snake_head.color('lightgreen')
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = 'stop'

# Generate food items
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x,y)

# Create snake body
snake_body = []

# Add a score variable
score = 0

# Functions to change direction
def move_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def move_down():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def move_left():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'

def move_right():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

# Function to move the snake
def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x+20)

def display_score():
    score_turtle = turtle.Turtle()
    score_turtle.speed(0)
    score_turtle.color('white')
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.goto(0,260)
    score_turtle.clear()
    score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))


# Set the key bindings
screen.listen()
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# Start the game loop
while True:
    screen.update()

    #Check for collision with borders
    if (snake_head.xcor() > 290 or snake_head.xcor() < -290 
    or snake_head.ycor() > 290 or snake_head.ycor() < -290):
        snake_head.goto(0,0)
        snake_head.direction = 'stop'

        # Hide the body
        for segment in snake_body:
            segment.goto(1000,1000)
        
        # Reset the score
        score = 0
        display_score()

        # Clear the snake_body list
        snake_body.clear()

    # Check for collision with food:
    if snake_head.distance(food) < 20:
        # Move the food to a random spot
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('lightgreen')
        new_segment.penup()
        snake_body.append(new_segment)

        # Add points to the score
        score += 10
        display_score()
    
    # Move the end segments first in reverse order
    for index in range(len(snake_body)-1, 0, -1):
        x = snake_body[index-1].xcor()
        y = snake_body[index-1].ycor()
        snake_body[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)
    
    move()

    # Check for head collision with the body segments
    for segment in snake_body:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = 'stop'

            # Reset the score
            score = 0
            display_score()

            # Hide the segments
            for segment in snake_body:
                segment.goto(1000, 1000)
            
            # Clear the snake_body list
            snake_body.clear()
    
    time.sleep(0.1)
screen.mainloop()
