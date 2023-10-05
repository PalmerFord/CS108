"""CS 108 Homework 6

This module implements a GUI controller for a raindrop simulation

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from figure import Model
from helpers import get_random_color


class Raindrops:
    """Raindrops runs a simulation of multiple particles apearing on a canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Raindrops'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,2,1])
        self.drawing.bg = "white"
        clear_button = PushButton(box, command=self.clear_particles,
                                 text='Clear', grid=[0, 1])
        quit_button = PushButton(box, command=app.destroy,
                                 text='Quit', grid=[1, 1])
        self.drawing.when_clicked = self.clear_particles
        app.repeat(30, self.draw_frame)
        
    def clear_particles(self):
        """Clears all particles"""
        self.drawing.clear()
        
    def draw_frame(self):
        radius = randint(5, 25)
        x = randint(25, self.drawing.width - 25)
        y = randint(25, self.drawing.height - 25)
        color = get_random_color()
        Model(x, y, radius, color).draw(self.drawing)

app = App()
Raindrops(app)
app.display()

