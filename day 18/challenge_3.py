from turtle import Turtle, Screen
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


jerry = Turtle()
jerry.speed("fastest")
screen = Screen()
screen.colormode(255)

# for _ in range(40):
while True:
    jerry.color(random_color())
    jerry.circle(100)
    jerry.setheading(jerry.heading() - 5)
    jerry.circle(100)
    if jerry.heading() == 0.0:
        break
    else:
        continue
    


screen.exitonclick()