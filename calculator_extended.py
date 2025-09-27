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
# Ask the user to enter the first number
first_number = turtle.textinput("Please enter a number", "First Number")

# Ask the user to enter the second number
second_number = turtle.textinput("Please enter a number", "Second Number")

# Find the sum of the numbers
sum_numbers = float(first_number) + float(second_number)

# Find the difference of the numbers
difference = float(first_number) - float(second_number)

# Find the product of the numbers
product = float(first_number) * float(second_number)

# Find the quotient of the numbers
quotient = float(first_number) / float(second_number)

# Round up the quotient to one decimal place
quotient = round(quotient, 1)

# Set the style for the pen
turtle.color('red')

# Set the style
style = ('Courier', 30, 'italic')

# Set the position of the turtle
turtle.sety(60)

# Display the sum
turtle.write(sum_numbers, font=style, align='center')

# Set the position of the turtle
turtle.sety(20)

# Display the sum
turtle.write(difference, font=style, align='center')

# Set the position of the turtle
turtle.sety(-20)

# Display the sum
turtle.write(product, font=style, align='center')

# Set the position of the turtle
turtle.sety(-60)

# Display the sum
turtle.write(quotient, font=style, align='center')

# Hide the turtle
turtle.hideturtle()

# End the program
turtle.done()
