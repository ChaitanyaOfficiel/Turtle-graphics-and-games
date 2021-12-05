#importing turtle
import turtle

pen = turtle.Turtle()

#Defining curve fucntion 
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

#defining heart function
def heart():
    pen.fillcolor('red')
    #filling the color
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    # left curve
    curve()
    pen.left(120)

    #right curve
    curve()
    pen.forward(112)

    pen.end_fill()

heart()

def txt():
    pen.up()
    pen.setpos(-150,100)
    pen.down()
    pen.color('black')
    pen.write("I", font=("Verdana",14,"bold"))

txt()

def text():
    pen.up()
    pen.setpos(150,100)
    pen.down()
    pen.color('black')
    pen.write("SUBSCRIBERS",font=("Verdana",14,"bold"))
text()

pen.ht()
