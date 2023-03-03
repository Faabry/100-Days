from turtle import Turtle
from time import sleep

class Game_on(Turtle):

    def __init__(self):
        super().__init__()
        self.countdown = 3
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.hideturtle()
        

    def start(self):
        while not self.countdown == 0:
            self.clear()
            self.write(f"{self.countdown}", align="center",
                        font=("Courier", 40, "normal"))
            sleep(1)
            self.countdown -= 1
            break

        # for i in range(3, 0, -1):
        #     self.write(str(i), align="center", font=("Arial", 24, "normal"))
        #     self.screen.delay(1000)  # atrasa a execução por 1 segundo
        #     self.clear()
        
        # self.write("GO!", align="center", font=("Arial", 24, "normal"))
        # self.screen.delay(1000)  # atrasa a execução por 1 segundo
        # self.clear()
        
        # # Chama a função que move o objeto após a contagem regressiva
        # ball = Ball()
        # self.screen.ontimer(ball.move(), 10)            
        
        