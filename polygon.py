import turtle as tr
from math import sin,cos,pi
r =200
inc=2*pi/100
t=0;n=1.5
for i in range(100):
    x1=r*sin(t);y1=r*cos(t)
    x2=r*sin(t+n);y2=r*cos(t+n)
    tr.speed('fast')
    tr.penup();tr.goto(x1,y1)
    tr.pendown();tr.goto(x2,y2)
    t+=inc

