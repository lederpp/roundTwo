

import turtle

cX, cY = eval(input("Enter the center point for a rectangle (separated by a comma): "))
w, h = eval(input("Enter the width and height (separated by a comma): "))

turtle.penup()
turtle.goto(cX, cY)
turtle.goto(0.5 * cX, 0.5 * cY)