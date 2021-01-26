import turtle
from random import randint

turtle.bgcolor("black")
turtle.color("white")

turns = 0
def draw_stars():
    for i in range(5):
        turtle.left(145)
        turtle.forward(10)

num_stars = 0
while num_stars < 40:
    x = randint(-300,200)
    y = randint(-300,200)
    draw_stars()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_stars = num_stars +1


turtle.write("GOOD NIGHT", font=("Sans-serif",30,"normal"))
