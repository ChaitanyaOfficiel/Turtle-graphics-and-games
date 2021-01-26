from turtle import *
speed(0)
setup(800,500)
title("Indian Flag")
penup()
goto(-400,250)
pendown()

# orange color
begin_fill()
color("orange")
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

#green color
left(90)
forward(167)

begin_fill()
color("green")
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

# Ashok chakra section
penup()
goto(70,0)
pendown()
color("navy")
begin_fill()
circle(70)
end_fill()

#white circle
penup()
goto(60,0)
pendown()
color("white")
begin_fill()
circle(60)
end_fill()

#small circle
penup()
goto(-57,-8)
pendown()
color("navy")
for i in range(24):
    begin_fill()
    circle(3)
    penup()
    forward(15)
    right(15)
    pendown()
    end_fill()

# inner circle
penup()
goto(20,0)
pendown()
color("navy")
begin_fill()
circle(20)
end_fill()

#spikes of wheel
penup()
goto(0,0)
pendown()
for i in range(24):
    forward(60)
    backward(60)
    left(15)

#Jai word
penup()
goto(-150,-50)
pendown()
write("Jai",font=("Verdana",30,"bold"))

#Hind word
penup()
goto(150,-50)
pendown()
write("Hind",font=("Verdana",30,"bold"))






