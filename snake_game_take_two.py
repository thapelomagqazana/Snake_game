import turtle 

# Set the game screen
screen = turtle.Screen()
# Give the screen a name
screen.title('Snake Game')
# Background colour of the screen
screen.bgcolor('lightgreen')

# Create a turtle as a snake head
snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.goto(0,0)

# Create snake body
snake_body = [turtle.Turtle()]
snake_body[0].shape("square")
snake_body[0].goto(snake_head.xcor(), snake_head.ycor()-20)


turtle.exitonclick()