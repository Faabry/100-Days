from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    #-------------------- TODO 1:Create a snake body --------------------
    def create_snake(self):

        for position in STARTING_POSITIONS: # [(0, 0), (-20, 0), (-40, 0)]
            self.add_segment(position)    
            


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    #-------------------- TODO 2:Move the snake --------------------
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
                x_cor = self.segments[seg_num - 1].xcor()
                y_cor = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)


    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)



            
