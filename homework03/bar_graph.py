"""CS 108 - Homework 3.0

Displays the values in a list of positive integers as a bar graph.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

import math
import random
from guizero import App, Drawing

app = App('Drawing Canvas', bg="white")

drawing = Drawing(app, width='fill', height='fill')

def get_data():
    """
    Collects  a minimum of one data entry from the user and returns a list of that data.
    """
    data = []
    while True:
        recent_input = int(input('integer (negative number to quit):'))
        if recent_input < 0 and len(data) == 0:
            print('Please enter at least one value.')
        elif recent_input > -1:
            data.append(recent_input)
        else:
            break
    return data
    
def get_random_color():
    """
    Returns a random color.
    """
    color = random.choice(['#ffffd9','#edf8b1','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8','#253494','#081d58'])
    return color

def draw_bar_graph():
    """
    Plots data points imputed by the user onto a bar graph drawn in guizero.
    """
    print('Please enter the data elements to graph.')
    data = get_data()
    graph_color = get_random_color()
    hight = drawing.master.height / len(data)
    for i in range(len(data)):
        drawing.rectangle(0, i * hight, (data[i] / max(data)) * drawing.master.width, (i * hight) + hight, color=graph_color, outline=True, outline_color="black")

draw_bar_graph()

app.display()