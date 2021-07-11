# Used exercise 2.23 and just added the number of "steps" to each turtle.circle

import turtle

radius = 6

turtle.penup()
turtle.goto(-radius / 2, radius + radius)
turtle.pendown()
turtle.circle(radius, steps = 6)

turtle.penup()
turtle.goto(-radius / 2, -radius + radius)
turtle.pendown()
turtle.circle(radius, steps = 6)

turtle.penup()
turtle.goto(-radius * 2.5, radius + radius)
turtle.pendown()
turtle.circle(radius, steps = 6)

turtle.penup()
turtle.goto(-radius * 2.5, -radius + radius)
turtle.pendown()
turtle.circle(radius, steps = 6)

turtle.done()
