# --------------------- TODO 3:Create snake food ---------------------

from turtle import Turtle
from random import randint


class Food(Turtle):
    
    def __init__(self):
        # Inhereting the Turtle methods and attributes
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
# ------------------------------------------------------------------