import colorgram
from turtle import Turtle, Screen, colormode
import random
colormode(255)
tim = Turtle()

#colors = colorgram.extract('image.jpg',25)
#diff_colors = []
#for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r,g,b)
#     diff_colors.append(tuple)
#print(diff_colors)

color_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59)]

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
tim.setheading(360)

def pattern():
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.fd(50)

for i in range(10):
    pattern()
    tim.setheading(180)
    tim.fd(550)
    for i in range(2):
        tim.right(90)
        tim.fd(50)


screen = Screen()
screen.exitonclick()
