from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from scoreboard import Line
from game_on import Game_on
from time import sleep

# Creating the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("My Pong Game")
screen.bgcolor("black")

# Creating de right and left paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Creating the ball
ball = Ball()
# Creating the scoreboard
score = Scoreboard()

line = Line()

game = Game_on()
        

# Making the paddles responsible
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeyrelease(r_paddle.stop_moving, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeyrelease(r_paddle.stop_moving, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeyrelease(l_paddle.stop_moving, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeyrelease(l_paddle.stop_moving, "s")

# Defining a variable to keep looping until it comes false
game_is_on = True

# Mainly program
while game_is_on:
    game.start()
    screen.update()
    game.clear()
    sleep(ball.speed_up)
    ball.move()
    # Detecting contact with y coordinates
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # Detecting the contact with the paddles and x coordinates 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < - 330:
        ball.bounce_x()
    

    # Increasing the score and defining a limit score to end up the game
    if ball.xcor() > 410:
        if score.l_score == 2:
            game_is_on = False
        else:
            ball.refresh()
            score.l_point()

    elif ball.xcor() < - 410:
        if score.r_score == 2:
            game_is_on = False
        else:
            ball.refresh()
            score.r_point()


screen.exitonclick()
