# Look Over - why not going back to center to write/display area?

import turtle

x, y = eval(input("Enter the coordinates of the center of a circle(separated by a comma): "))
r = eval(input("Enter the radius of a circle: "))

PI = 3.14159
area = PI * r ** 2

turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(area)

turtle.hideturtle()
turtle.done()