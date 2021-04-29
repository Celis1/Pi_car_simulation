from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty,
    ObjectProperty,ListProperty,StringProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from random import randint
import numpy as np
from kivy.core.window import Window

#from Car import Car
from Sensor_manager import SensorManager
#testing
#from old_files.Sensor_manager_old import SensorManager
from Brain.ai import get_action
from Car import Bot
#Builder.load_file('Styles/main.kv')

window_width = Window.width# width of the map (horizontal edge)
window_height = Window.height
sand = np.zeros((window_width,window_height)) # initializing the sand array with only zeros

class MyPaintWidget(Widget):
    def on_touch_down(self, touch): # putting some sand when we do a left click
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.5,0.7,0.2)
            #d = 10.0
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1

    def on_touch_move(self, touch): # putting some sand when we move the mouse while pressing left
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            #density = n_points/(length)
            #touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y
