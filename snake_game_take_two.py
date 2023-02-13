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
        
        # Clear the body list
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

            # Hide the segments
            for segment in snake_body:
                segment.goto(1000, 1000)
            
            # Clear the snake_body list
            snake_body.clear()
    
    time.sleep(0.1)
screen.mainloop()
# currennt_direction = 'Up'

# # Control the snake's directions
# def move_up():
#     global current_direction
#     current_direction = 'Up'
#     if current_direction != 'Down':
#         snake_head.setheading(90)
#         snake_head.forward(20)
#         new_segment = turtle.Turtle()
#         new_segment.shape('square')
#         new_segment.penup()
#         new_segment.goto(snake_head.xcor(), snake_head.ycor())
#         snake_body.append(new_segment)
#         if len(snake_body) > 1:
#             last_segment = snake_body.pop()
#             last_segment.clear()
#             del last_segment

# def move_left():
#     global current_direction
#     current_direction = 'Left'
#     if current_direction != 'Right':
#         snake_head.setheading(180)
#         snake_head.forward(20)
#         new_segment = turtle.Turtle()
#         new_segment.shape('square')
#         new_segment.penup()
#         new_segment.goto(snake_head.xcor(), snake_head.ycor())
#         snake_body.append(new_segment)
#         if len(snake_body) > 1:
#             last_segment = snake_body.pop()
#             last_segment.clear()
#             del last_segment

# def move_down():
#     global current_direction
#     current_direction = 'Down'
#     if current_direction != 'Up':
#         snake_head.setheading(270)
#         snake_head.forward(20)
#         new_segment = turtle.Turtle()
#         new_segment.shape('square')
#         new_segment.penup()
#         new_segment.goto(snake_head.xcor(), snake_head.ycor())
#         snake_body.append(new_segment)
#         if len(snake_body) > 1:
#             last_segment = snake_body.pop()
#             last_segment.clear()
#             del last_segment


# def move_right():
#     global current_direction
#     current_direction = 'Right'
#     if current_direction != 'Left':
#         snake_head.setheading(0)
#         snake_head.forward(20)
#         new_segment = turtle.Turtle()
#         new_segment.shape('square')
#         new_segment.penup()
#         new_segment.goto(snake_head.xcor(), snake_head.ycor())
#         snake_body.append(new_segment)
#         if len(snake_body) > 1:
#             last_segment = snake_body.pop()
#             last_segment.clear()
#             del last_segment


# screen.onkeypress(move_up, 'Up')
# screen.onkeypress(move_down, 'Down')
# screen.onkeypress(move_left, 'Left')
# screen.onkeypress(move_right, 'Right')
# screen.listen()

# turtle.exitonclick()
# while True:
#     if current_direction == 'Up':
#         screen.ontimer(move_up, t=100)
#     elif current_direction == 'Down':
#         screen.ontimer(move_down, t=100)
#     elif current_direction == 'Left':
#         screen.ontimer(move_left, t=100)
#     elif current_direction == 'Right':
#         screen.ontimer(move_right, t=100)

