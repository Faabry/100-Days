from turtle import Turtle

STARTING_POSITION = [(350, 0), (0, 350)]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setposition(position)
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


    def stop_moving(self):
        pass