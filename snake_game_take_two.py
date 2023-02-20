import turtle
import random
import time
import math

delay = 0.1

# Set the game screen
screen = turtle.Screen()
# Give the screen a name
screen.title('Snake Game')
screen.setup(width=600, height=600)
# Background colour of the screen
screen.bgcolor('lightgreen')

# Set up the game border
border = turtle.Turtle()
border.speed(0)
border.color('black')
border.penup()
border.setposition(-300,300)
border.pendown()
border.pensize(4)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()


# Create a turtle as a snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape('square')
snake_head.color('darkgreen')
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = 'stop'

# The initial speed of the snake
snake_speed = 5

# Define the current speed of the snake
current_speed = snake_speed

# Generate food items
# food = turtle.Turtle()
# food.speed(0)
# food.shape('circle')
# food.color('red')
# food.penup()
# x = random.randint(-290, 290)
# y = random.randint(-290, 290)
# food.goto(x,y)

# Set up the food items
food_list = []
foods = {
    'normal': {
    'colour': 'red',
    'points': 10,
    'size': 20
    },
    'big': {
    'colour': 'purple',
    'points': 20,
    'size': 40
    },
    'small': {
    'colour': 'blue',
    'points': 5,
    'size': 10
    },
    'fast': {
    'colour': 'orange',
    'size': 20,
    'points': 15,
    'effect': 'speed_up'
    },
    'slow': {
    'colour': 'gray',
    'size': 20,
    'points': 15,
    'effect': 'speed_down'
    }
}

# Create snake body
snake_body = []

# Create food list



# Set up the score display
score = 0
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color('black')
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0,260)
score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

def reset_speed():
    global current_speed
    current_speed = snake_speed

def apply_effect(effect):
    if effect == 'speed_up':
        # Double the snake's speed for 10 seconds
        global snake_speed
        snake_speed *= 2
        turtle.ontimer(reset_speed,10000)
    elif effect == 'shrink':
        global snake_body
        if len(snake_body) > 1:
            snake_body.pop()

def create_food():
    # Generate a random type of food
    food_type = random.choice(list(foods.keys()))
    food_props = foods[food_type]

    # Create the food turtle
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color(food_props['colour'])
    food.penup()
    food.shapesize(food_props['size']/20)

    # Set the food's position
    food_x = random.randint(-290,290)
    food_y = random.randint(-290,290)
    food.goto(food_x,food_y)

    # Add the food to a list of foods
    food_list.append(food)

    # Set the food's point value
    food_point = food_props['points']

    # Apply any special effects
    if 'effect' in food_props:
        effect = food_props['effect']
        apply_effect(effect)

    return food_point

# Generate initial food items:
points = create_food()

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

def is_collison(t1,t2):
    # Calculate the distance between the two turtles.
    x_distance = t1.xcor() - t2.xcor()
    y_distance = t1.ycor() - t2.ycor()
    distance = math.sqrt(x_distance**2 + y_distance**2)

    # If the distance is less than the combined size of turtles, there is a collision
    if distance < 20:
        return True
    else:
        return False
# def display_score():
#     score_turtle = turtle.Turtle()
#     score_turtle.speed(0)
#     score_turtle.color('white')
#     score_turtle.penup()
#     score_turtle.hideturtle()
#     score_turtle.goto(0,310)
#     score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))


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
        score_turtle.clear()
        score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

        # Clear the snake_body list
        snake_body.clear()

    # Check for collision with food:
    for foodA in food_list:
        if is_collison(snake_head,foodA):
            food_point = create_food()
            score += food_point

    # if snake_head.distance(food) < 20:
    #     # Move the food to a random spot
    #     food.goto(random.randint(-290, 290), random.randint(-290, 290))

    #     new_segment = turtle.Turtle()
    #     new_segment.speed(0)
    #     new_segment.shape('square')
    #     new_segment.color('lightgreen')
    #     new_segment.penup()
    #     snake_body.append(new_segment)

    #     # Add points to the score
    #     score += 10
            score_turtle.clear()
            score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
    
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
            score_turtle.clear()
            score_turtle.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

            # Hide the segments
            for segment in snake_body:
                segment.goto(1000, 1000)
            
            # Clear the snake_body list
            snake_body.clear()
    
    time.sleep(delay)
screen.mainloop()
