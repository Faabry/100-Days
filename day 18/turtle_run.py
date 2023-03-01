from turtle import Turtle, Screen


def forwards():
    harold.forward(10)


def backwards():
    harold.backward(10)


def counter_clock():
    new_position = harold.heading() + 10
    harold.setheading(new_position)


def clock_wise():
    new_position = harold.heading() - 10
    harold.setheading(new_position)


def clear():
    harold.clear()
    harold.penup()
    harold.home()
    harold.pendown()


harold = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()