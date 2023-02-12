import turtle
import random

# Set the game screen
screen = turtle.Screen()
# Give the screen a name
screen.title('Snake Game')
# Background colour of the screen
screen.bgcolor('lightgreen')

# Create a turtle as a snake head
snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.penup()
snake_head.goto(0,0)

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

current_direction = 'Up'

# Control the snake's directions
def move_up():
    global current_direction
    current_direction = 'Up'
    if current_direction != 'Down':
        snake_head.setheading(90)
        snake_head.forward(20)
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(snake_head.xcor(), snake_head.ycor())
        snake_body.append(new_segment)
        if len(snake_body) > 1:
            last_segment = snake_body.pop()
            last_segment.clear()
            del last_segment

def move_left():
    global current_direction
    current_direction = 'Left'
    if current_direction != 'Right':
        snake_head.setheading(180)
        snake_head.forward(20)
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(snake_head.xcor(), snake_head.ycor())
        snake_body.append(new_segment)
        if len(snake_body) > 1:
            last_segment = snake_body.pop()
            last_segment.clear()
            del last_segment

def move_down():
    global current_direction
    current_direction = 'Down'
    if current_direction != 'Up':
        snake_head.setheading(270)
        snake_head.forward(20)
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(snake_head.xcor(), snake_head.ycor())
        snake_body.append(new_segment)
        if len(snake_body) > 1:
            last_segment = snake_body.pop()
            last_segment.clear()
            del last_segment


def move_right():
    global current_direction
    current_direction = 'Right'
    if current_direction != 'Left':
        snake_head.setheading(0)
        snake_head.forward(20)
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(snake_head.xcor(), snake_head.ycor())
        snake_body.append(new_segment)
        if len(snake_body) > 1:
            last_segment = snake_body.pop()
            last_segment.clear()
            del last_segment


screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.listen()

turtle.exitonclick()
while True:
    if current_direction == 'Up':
        screen.ontimer(move_up, t=100)
    elif current_direction == 'Down':
        screen.ontimer(move_down, t=100)
    elif current_direction == 'Left':
        screen.ontimer(move_left, t=100)
    elif current_direction == 'Right':
        screen.ontimer(move_right, t=100)

