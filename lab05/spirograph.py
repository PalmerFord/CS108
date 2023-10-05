"""CS 108 - Lab 5.2

Draws a spirograph according to user inputs

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall, 2021
"""

import math
from guizero import App, Drawing
from time import sleep

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

moving_radius = float(input('moving radius: '))
fixed_radius = float(input('fixed radius: '))
pen_offset = float(input('pen offset: '))
color = input('color: ')
center = app.width / 2

# defines the starting point of the spirograph
x = fixed_radius + moving_radius + pen_offset + center
y = center

# draws the spirograph
t = 0.0
while t < 360:
    t += 0.1
    next_x = (fixed_radius + moving_radius) * math.cos(t) + pen_offset * math.cos(((fixed_radius + moving_radius) * t) / moving_radius) + center
    next_y = (fixed_radius + moving_radius) * math.sin(t) + pen_offset * math.sin(((fixed_radius + moving_radius) * t) / moving_radius) + center
    drawing.line(x, y, next_x, next_y, color)
    x = next_x
    y = next_y
    app.update()
    
app.display()
