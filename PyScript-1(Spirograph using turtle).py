import random
import turtle

tur=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
tur.pencolor("yellow")
tur.speed(0)
a=0
colors=["red","orange","yellow","green","blue","indigo","violet"]
while True:
    for i in range(8):
        tur.color(random.choice(colors))
        tur.forward(50)
        tur.right(45)
    tur.right(10)
    a = a+1
    if a >= 360/10:
        break
turtle.done()
