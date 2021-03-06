# Look Over - say in the center of the screen, this draws them all in (-x, -y)
# Modified to have all circles based on center (0, 0)

import turtle

radius = eval(input("Enter a radius for a circle: "))

turtle.penup()
turtle.goto(-radius / 2, radius + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius / 2, -radius + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius * 2.5, radius + radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius * 2.5, -radius + radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()
