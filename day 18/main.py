# Turtle challenge 
# Draw a: 
#TODO 1: triangle = 3 sides 
#TODO 2: square = 4 sides
#TODO 3: pentagon = 5 sides 
#TODO 4: hexagon = 6 sides 
#TODO 5: heptagon = 7 sides
#TODO 6: otagon = 8 sides
#TODO 7: monagon = 9 sides
#TODO 8: decagon = 10 sides


from turtle import Turtle
from turtle import Screen
from turtle import color
from random import choice

# ------------------- Main Program ------------------
tommy = Turtle()
colors = ["red", "blue", "yellow", "green", "black", "purple", "gray", "brown"]

number_of_sides = 3

while not number_of_sides == 10:
    tommy.color(choice(colors))
    for _ in range(number_of_sides):
        angle = 360 / number_of_sides
        tommy.forward(100)
        tommy.right(angle)
    number_of_sides += 1
# ---------------- End of Program --------------------