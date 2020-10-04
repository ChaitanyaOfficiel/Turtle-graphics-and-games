from turtle import *

circle(120, 360/2)

begin_fill()
circle(120, 360/2)
end_fill()

pu(); lt(90); fd(60)
dot(120, 'white'); dot(35, 'black')
fd(120)
dot(120, 'black'); dot(35, 'white')

ht(); done()