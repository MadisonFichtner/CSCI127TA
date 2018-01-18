import turtle
import random

window = turtle.Screen()

square = turtle.Turtle() # define the turtle responsible for drawing the square
square.speed(0) # make the turtle draw at light-speed
square.hideturtle() # make the turtle itself invisible

# draw_square performs all the drawing relating to the on-screen square
def draw_square():
    square.up()
    square.goto(-200, 200)
    square.down()

    for _ in range(4):
        square.forward(50)
        square.right(90)
draw_square()
square.up()
square.goto(-205, 205)
square.write("Change Color")

pencil = turtle.Turtle() # define the turtle that will be the color-changing pencil
pencil.shape("circle") # make the turtle look like a dot

# drawing_controls changes the pencil to a random color
#   when a user clicks inside the square
def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        red = random.random()
        green = random.random()
        blue = random.random()
        pencil.color(red, green, blue)
        square.color(red, green, blue)
        draw_square()

window.onclick(drawing_controls) # call drawing_controls whenever the user clicks the turtle window

pencil.onrelease(pencil.goto)
turtle.done() # ensure the file can run on the command line
