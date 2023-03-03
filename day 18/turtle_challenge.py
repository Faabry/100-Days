# TODO 1: Draw a square with turtle


def draw_square():
    for c in range(0, 4):
        regis.forward(100)
        regis.right(90)
        regis.forward(100)


from turtle import Turtle, Screen

regis = Turtle()
regis.shape("turtle")
regis.color("blue", "red")
draw_square()

screen = Screen()
screen.exitonclick()


