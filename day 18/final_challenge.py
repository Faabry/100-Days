from turtle import Turtle, Screen
import colorgram
from random import choice


# Extract 6 colors from the image
original_colors = colorgram.extract("paint.jpg", 30)
colors = []
for color in original_colors:
    colors.append(color.rgb)

rgb = []
for c in colors:
    r = c.r
    g = c.g
    b = c.b 
    rgb.append([r, g, b])

rgb = [tuple(i) for i in rgb]
color_list = [(199, 176, 116), (125, 36, 24), (208, 220, 212), (167, 106, 56), (185, 157, 54), (5, 56, 82), (221, 225, 228), (107, 68, 86), (42, 35, 34), (112, 161, 174), (22, 121, 172), (89, 142, 54), (76, 39, 48), (63, 153, 139), (8, 67, 47), (181, 96, 80), (134, 40, 43), (212, 201, 150), (144, 173, 159), (174, 153, 158), (179, 201, 187), (213, 182, 176), (206, 183, 186), (95, 138, 154), (42, 74, 62), (143, 118, 122), (168, 198, 212), (38, 74, 82)]


tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.penup()
tom.goto(-200, 200)


height = 200
for c in range(0, 6):
    for c in range(0, 5):
        tom.dot(30, choice(color_list))
        tom.forward(60)
    tom.goto(-200, height)
    height -= 50

screen.exitonclick()





