"""CS 108 - Homework 2.12

Draws the French flag 

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

UNIT = int(input('Size of the flag: '))

import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)

# Centers the flag
pen.up()
pen.right(90)
pen.forward(UNIT)
pen.right(90)
pen.forward(UNIT * 0.5)
pen.down()

# Draws the blue portion of the flag
pen.pencolor('#0055A4')
pen.fillcolor('#0055A4')
pen.begin_fill()
pen.forward(UNIT)
pen.right(90)
pen.forward(UNIT * 2)
pen.right(90)
pen.forward(UNIT)
pen.right(90)
pen.forward(UNIT * 2)
pen.end_fill()

# Draws the red portion of the flag
pen.up()
pen.right(270)
pen.forward(UNIT)
pen.pencolor('#EF4135')
pen.fillcolor('#EF4135')
pen.down()
pen.begin_fill()
pen.forward(UNIT)
pen.right(270)
pen.forward(UNIT * 2)
pen.right(270)
pen.forward(UNIT)
pen.right(270)
pen.forward(UNIT * 2)
pen.end_fill()

# Draws the white portion of the flag
pen.pencolor('black')
pen.right(90)
pen.forward(UNIT)
pen.up()
pen.right(90)
pen.forward(UNIT * 2)
pen.down()
pen.right(90)
pen.forward(UNIT)