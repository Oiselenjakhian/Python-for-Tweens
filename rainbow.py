"""
Developer Name: Truston Ailende
Email Address: trustonailende@gmail.com
"""
import turtle
import math
 
# Square
def drawSquare(length):
    turtle.penup()
    turtle.setposition(-length/2.0, length/2.0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()
    turtle.home()
 
# Horizontal lines
def drawHorizontalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    for j in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(-half, j)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Vertical lines
def drawVerticalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    turtle.right(90)
    for k in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(k, half)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Draw the grid
turtle.speed(1000000)
drawSquare(400)
drawHorizontalLine(400, 40)
drawVerticalLine(400, 40)
 
# Change the colour mode
turtle.colormode(255)
 
# Change the pencolor to red
turtle.pencolor(255, 0, 0)
 
# Draw the horizontal centre line
turtle.setposition(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.penup()
 
# Draw the vertical centre line
turtle.setposition(0, 200)
turtle.setheading(270)
turtle.pendown()
turtle.forward(400)
 
# Reset all the properties
turtle.home()
turtle.pencolor(0, 0, 0)
 
# Place code here
turtle.pensize(12)
turtle.setheading(90)

turtle.penup()
turtle.setposition(130, 0)
turtle.pendown()
turtle.pencolor(46, 0, 153)
turtle.circle(130, 180)

turtle.penup()
turtle.setposition(140, 0)
turtle.pendown()
turtle.pencolor(0, 0, 129)
turtle.setheading(90)
turtle.circle(140, 180)

turtle.penup()
turtle.setposition(150, 0)
turtle.pendown()
turtle.pencolor(0, 155, 253)
turtle.setheading(90)
turtle.circle(150, 180)

turtle.penup()
turtle.setposition(160, 0)
turtle.pendown()
turtle.pencolor(0, 187, 0)
turtle.setheading(90)
turtle.circle(160, 180)

turtle.penup()
turtle.setposition(170, 0)
turtle.pendown()
turtle.pencolor(249, 245, 3)
turtle.setheading(90)
turtle.circle(170, 180)

turtle.penup()
turtle.setposition(180, 0)
turtle.pendown()
turtle.pencolor(254, 97, 47)
turtle.setheading(90)
turtle.circle(180, 180)

turtle.penup()
turtle.setposition(190, 0)
turtle.pendown()
turtle.pencolor(218, 1, 0)
turtle.setheading(90)
turtle.circle(190, 180)
 
# End the program
turtle.done()
