from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))
        
    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.draw_line()

    def draw_line(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        x = 0
        y = 300
        
        for _ in range(200):
            self.goto(x, y)
            self.write("|")
            y -= 10

            