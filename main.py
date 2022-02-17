import turtle               #1. import modules
import random

def draw_polygon(num_sides = 3, side_len = 40):
  turn_angle = 360/num_sides

  for i in range(num_sides):
    leonardo.forward(side_len)
    leonardo.left(turn_angle)

def clear_turtle_drawings(my_turtle = None):
  my_turtle.clear()

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
#1st method Turtle Race
michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#2nd method Turtle Race
for i in range(10):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


## Part B - complete part B here
#Equilateral Triangle (3)
leonardo.down()
side_len = 90
num_sides = 3

draw_polygon(num_sides, side_len)
clear_turtle_drawings(leonardo)

#Square (4)
side_len = 80
num_sides = 4

draw_polygon(num_sides, side_len)
clear_turtle_drawings(leonardo)

#Hexagon (6)
side_len = 75
num_sides = 6

draw_polygon(num_sides, side_len)
clear_turtle_drawings(leonardo)

#Nonagon (9)
side_len = 50
num_sides = 9

draw_polygon(num_sides, side_len)
clear_turtle_drawings(leonardo)

#Dodecagon (12)
side_len = 40
num_sides = 12

draw_polygon(num_sides, side_len)
clear_turtle_drawings(leonardo)

window.exitonclick()