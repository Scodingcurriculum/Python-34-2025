#Start code here
from turtle import *
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
r = 150
turtle = Turtle()
screen = Screen()
screen.bgcolor("skyblue")
turtle.setheading(-90)
turtle.speed(0)
turtle.fillcolor(255, 0, 0)
turtle.width(30)
x = 150
for color in colors:
  turtle.color(color)
  turtle.penup()
  turtle.goto(x, -100)
  turtle.setheading(90)
  turtle.pendown()
  turtle.circle(r,180)
  r -= 15
  x -= 1
