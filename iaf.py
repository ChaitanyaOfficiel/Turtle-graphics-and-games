from turtle import *
speed(0)
setup(800,500)

bgcolor("skyblue")
title("Indian Air Force Flag")

penup()
goto(-400,250)
pendown()

#orange
color("orange")
begin_fill()               
forward(250)
right(90)
forward(83)
right(90)
forward(250)
end_fill()

left(90)
#white
color("white")
begin_fill()               
forward(83)
left(90)
forward(250)
left(90)
forward(83)
end_fill()

left(180)
penup()
forward(83)
pendown()
#green
color("green")
begin_fill()               
forward(83)
right(90)
forward(250)
right(90)
forward(83)
end_fill()

#navy circle
penup()
goto(-260,125)
pendown()
color('navy')
begin_fill()
circle(30)
end_fill()

#white circle
penup()
goto(-270,125)
pendown()
color("white")
begin_fill()
circle(20)
end_fill()

#chakra
penup()
goto(-290,125)
pendown()
color('navy')
for i in range(24):
    forward(20)
    backward(20)
    left(15)

#orange circle
penup()
goto(200,-100)
pendown()
color("orange")
begin_fill()
circle(70)
end_fill()

#white circle
penup()
goto(190,-100)
pendown()
color('white')
begin_fill()
circle(60)
end_fill()

#green circle
penup()
goto(180,-100)
pendown()
color('green')
begin_fill()
circle(50)
end_fill()
