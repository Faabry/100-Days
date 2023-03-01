from turtle import Turtle
from turtle import Screen
from random import choice
from random import randint


def random_color():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    color = (R, G, B)
    return color

john = Turtle()
john.pensize(10)
john.speed(50)
screen = Screen()
screen.colormode(255)

# colors = ["red", "blue", "yellow", "green", "gray", "black", "brown", "orange"]
directions = [0, 90, 180, 270]

for _ in range(400):
    john.color(random_color())
    john.forward(20)
    john.setheading(choice(directions))
screen.exitonclick()


