import turtle
turtle.speed(0)
turtle.setup(800,500)

turtle.pensize(14)
turtle.pencolor("black")

#invisiable cloak
turtle.circle(62)

#stone
for i in range(3):
    turtle.forward(120)
    turtle.left(120)
    turtle.forward(120)


#elder wand
turtle.right(-90)
turtle.forward(200)
