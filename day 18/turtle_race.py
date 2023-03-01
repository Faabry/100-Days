from turtle import Turtle, Screen, forward
from random import randint

race_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput("Make your bet:",
                 "Which turtle will win the race? Enter with a color:")
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
turtle_list = []

if user_guess:
    race_is_on = True

x = -230
y = -100

for index in range(6):
        timmy = Turtle(shape="turtle")
        timmy.penup()
        timmy.color(colors[index])
        timmy.goto(x, y)
        turtle_list.append(timmy)
        y += 40
while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
             race_is_on = False
             if user_guess == turtle.color():
                  print("You win\n" +
                        f"Your guess: {user_guess} | Turtle winner: {turtle.pencolor()}")
             else:
                  print(f"You lose!\n"+
                        f"Your guess: {user_guess} | Turtle winner: {turtle.pencolor()}")
        else:
            random_distance = randint(0, 10)
            turtle.forward(random_distance)
screen.exitonclick()

