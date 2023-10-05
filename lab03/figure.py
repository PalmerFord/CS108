"""CS 108 - Lab 3.3

draws a stick figure

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall, 2021
"""

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

unit = 50                # Change this value to rescale the drawing.

# draws the head
drawing.oval(
    1 * unit, 2 * unit,  # bounding box x1, y1
    3 * unit, 4 * unit,  # bounding box x2, y2
    outline=True,
    color='blue'
)

# draws the arms
drawing.line(
    1 * unit, 5 * unit, # x1, y1
    3 * unit, 5 * unit, # x2, y2
    color='blue'
)

# draws the body
drawing.line(
    2 * unit, 4 * unit,  # x1, y1
    2 * unit, 6 * unit,  # x2, y2
    color='blue'
)

# draws the left leg
drawing.line(
    1 * unit, 7 * unit,  # x1, y1
    2 * unit, 6 * unit,  # x2, y2
    color='blue'
)

#draws the right leg
drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    3 * unit, 7 * unit,  # x2, y2
    color='blue'
)

app.display()
