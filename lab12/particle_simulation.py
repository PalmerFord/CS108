"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Particle Simulation'
        UNIT = 900
        CONTROL_UNIT = 50
        app.width = UNIT * 2
        app.height = UNIT + CONTROL_UNIT

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT * 2, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT * 2, height=UNIT, grid=[0,0,1,1])
        self.drawing.bg = "black"
        particle_button = PushButton(box, command=self.add_particle,
                                 text='Add particle', grid=[0, 1])
        self.p_list = []
        self.drawing.when_clicked = self.check_remove_particle
        app.repeat(10, self.draw_frame)
        
    def add_particle(self):
        """Creates a new particle"""
        radius = randint(5, 25)
        x = randint(25, self.drawing.width - 25)
        y = randint(25, self.drawing.height - 25)
        vel_x = randint(-radius // 10, radius // 10)
        vel_y = randint(-radius // 10, radius // 10)
        color = get_random_color()
        self.p_list.append(Particle(x, y, vel_x, vel_y, radius, color))
        
    def draw_frame(self):
        """Draws and animates all particles"""
        self.drawing.clear()
        for i in self.p_list:
            i.move(self.drawing)        
        for i in range(len(self.p_list)):
            for j in range(i):
                self.p_list[i].bounce(self.p_list[j])
        for p in self.p_list:
            p.draw(self.drawing)
            
    def check_remove_particle(self, event):
        """removes any particle if it has been clicked"""
        copy = self.p_list[:]
        for p in copy:
            if p.is_clicked(event.x, event.y):
                self.p_list.remove(p)
            

app = App()
ParticleSimulation(app)
app.display()

