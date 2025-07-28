#Start code here
import random
from turtle import *
screen = Screen()
screen.bgcolor("black")
turtle = Turtle()
turtle.speed(10)
turtle.width(2)
for i in range(30, 360, 5):
  turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  turtle.forward(i)
  turtle.right(108)
#Additonally explore output with different angles to draw different shape spirals # your own code
#Instead of turn right by 108 degrees, try values like 119, 89 # your own code
