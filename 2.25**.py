# Look Over

import turtle

cX, cY = eval(input("Enter the center point for a rectangle (separated by a comma): "))
w, h = eval(input("Enter the width and height (separated by a comma): "))

turtle.penup()
turtle.goto(cX - 0.5 * w, cY + 0.5 * h)
turtle.pendown()
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)

turtle.done()