from turtle import Screen
from snake import Snake
from scoreboard import Score
from food import Food
from time import sleep


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    
    #TODO 4:Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #TODO 6:Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #TODO 7:Detec collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()