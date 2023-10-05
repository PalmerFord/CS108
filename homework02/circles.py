"""CS 108 - Homework 2.0

Given the parameters of two circles, the code draws them and determines if they
are disjointed, overlaping, circle 1 contains circle 2, or circle 2 contains circle 1

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

import math
from guizero import App, Drawing

app = App('Drawing Canvas', bg="white")

drawing = Drawing(app, width='fill', height='fill')

circle1x = int(input('Circle 1 x:'))
circle1y = int(input('Circle 1 y:'))
circle1radius = int(input('Circle 1 radius:'))

circle2x = int(input('Circle 2 x:'))
circle2y = int(input('Circle 2 y:'))
circle2radius = int(input('Circle 2 radius:'))

# Calculates the Distance between the Center Points
dcp = math.sqrt((abs(circle1x - circle2x) ** 2) + (abs(circle1y - circle2y) ** 2))

# Draws the larger circle first to prevent one from covering the other
if circle2radius > circle1radius:
    drawing.oval(circle2x - circle2radius, circle2y - circle2radius,
                 circle2x + circle2radius, circle2y + circle2radius,
                 color="white", outline=True)
    drawing.oval(circle1x - circle1radius, circle1y - circle1radius,
                 circle1x + circle1radius, circle1y + circle1radius,
                 color="white", outline=True)
else:
    drawing.oval(circle1x - circle1radius, circle1y - circle1radius,
                 circle1x + circle1radius, circle1y + circle1radius,
                 color="white", outline=True)
    drawing.oval(circle2x - circle2radius, circle2y - circle2radius,
                 circle2x + circle2radius, circle2y + circle2radius,
                 color="white", outline=True)

# Determines whether the circles are disjointed, overlaping, circle 1 contains circle 2, or circle 2 contains circle 1
if dcp > (circle1radius + circle2radius):
    print('The circles are disjoint.')
elif (dcp + circle2radius) < circle1radius:
    print('Circle 1 contains circle 2.')
elif (dcp + circle1radius) < circle2radius:
    print('Circle 2 contains circle 1.')
else:
    print('The circles overlap.')

app.display()