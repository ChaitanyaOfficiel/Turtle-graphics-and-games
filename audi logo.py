from turtle import *
speed(0)
setup(800,500)
title('Audilogo')
bgcolor('black')

#first circle
pensize(12)
pencolor('white')
circle(80)

#second circle
penup()
goto(-120,0)
pendown()
pencolor('white')
circle(80)

#thrid color
penup()
goto(-240,0)
pendown()
pencolor('white')
circle(80)

#fourth color
penup()
goto(120,0)
pendown()
pencolor('white')
circle(80)
