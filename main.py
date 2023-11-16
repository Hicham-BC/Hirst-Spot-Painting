from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract

colors = extract("Hirst-spot-painting.png", 20)

rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

colormode(255)

timmy = Turtle(shape="circle")
timmy.shapesize(1, 1)
timmy.speed(10)
timmy.penup()

y_cor = -210
row = 0
while row < 10:
    column = 0
    timmy.setposition(-240, y_cor)

    while column < 10:
        random_color = choice(rgb)
        timmy.color(random_color)
        timmy.stamp()
        if column < 9:
            timmy.forward(50)
        column += 1
    y_cor += 50
    row += 1


screen = Screen()
screen.exitonclick()