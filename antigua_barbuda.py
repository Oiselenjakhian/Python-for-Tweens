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
turtle.pencolor(0, 0, 0)
turtle.begin_fill()
turtle.penup()
turtle.setposition(-200, 135)
turtle.pendown()
turtle.setposition(200, 135)
turtle.setposition(125, 40)
turtle.setposition(-125, 40)
turtle.setposition(-200, 135)
turtle.end_fill()

turtle.color(255, 213, 0)
turtle.begin_fill()
turtle.penup()
turtle.setposition(-75, 40)
turtle.pendown()
turtle.setposition(-45, 45)
turtle.setposition(-65, 65)
turtle.setposition(-35, 65)
turtle.setposition(-55, 90)
turtle.setposition(-25, 80)
turtle.setposition(-20, 110)
turtle.setposition(-10, 85)
turtle.setposition(0, 115)
turtle.setposition(10, 85)
turtle.setposition(20, 110)
turtle.setposition(25, 80)
turtle.setposition(55, 90)
turtle.setposition(35, 65)
turtle.setposition(65, 65)
turtle.setposition(45, 45)
turtle.setposition(75, 40)
turtle.setposition(-75, 40)
turtle.end_fill()

turtle.color(51, 170, 255)
turtle.begin_fill()
turtle.penup()
turtle.setposition(-125, 40)
turtle.pendown()
turtle.setposition(-80, -20)
turtle.setposition(80, -20)
turtle.setposition(125, 40)
turtle.setposition(-125, 40)
turtle.end_fill()

turtle.color(255, 255, 255)
turtle.begin_fill()
turtle.penup()
turtle.setposition(-80, -20)
turtle.pendown()
turtle.setposition(0, -130)
turtle.setposition(80, -20)
turtle.setposition(-80, -20)
turtle.end_fill()

turtle.color(204, 0, 51)
turtle.begin_fill()
turtle.penup()
turtle.setposition(-200, 135)
turtle.setposition(10, -130)
turtle.setposition(-200, -130)
turtle.setposition(-200, 135)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.setposition(200, 135)
turtle.setposition(-10, -130)
turtle.setposition(200, -130)
turtle.setposition(200, 135)
turtle.end_fill()

turtle.hideturtle()
 
# End the program
turtle.done()
