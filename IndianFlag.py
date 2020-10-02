from turtle import *
speed(0)
setup(800, 500)
title("Indian Flag")
penup()
goto(-400, 250)
pendown()
# orange color
begin_fill()

color("Orange")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()


left(90)
forward(167)

#green color
color("Green")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()


#main circle
penup()
goto(70,0)
color("navy")
pendown()
begin_fill()
circle(70)
end_fill()
#white circle
penup()
goto(60,0)
color("white")
pendown()
begin_fill()
circle(60)
end_fill()
#wheel like look
penup()
goto(-57, -8)
pendown()
color("navy")
for i in range(24):
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(15)
    right(15)
    pendown()
#inner circle
penup()
goto(20,0)
pendown()
begin_fill()
circle(20)
end_fill()
#spikes of wheel
penup()
goto(0, 0)
pendown()
for i in range(24):
    forward(60)
    backward(60)
    left(15)
hideturtle()


