from turtle import Turtle
from time import sleep


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_up = 0.1

    def move(self):
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x_coordinate, y_coordinate)

    def bounce_y(self):
        self.y_move *= -1 #Becomes equals to -10

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.9

    def refresh(self):
        sleep(1)
        self.setposition(0, 0)
        self.speed_up = 0.1
        self.bounce_x()
        