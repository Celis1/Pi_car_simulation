from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty
from kivy.graphics import *
import math

''' creating each sensor here then using Sensor Manager to edit them'''
class Sensor(Widget):
    update = BooleanProperty(False)
    def __init__(self,points,car_pos,name ='Noname',**kwargs):
        super(Sensor,self).__init__(**kwargs)
        #using these values evertime update is called
        self.x1 = points[0]
        self.y1 = points[1]
        self.x2 = points[2]
        self.y2 = points[3]
        self.name = name #just incase
        self.car_pos = car_pos
        self._draw_line() #only should be called once
        self.bind(update=self.redraw) #if the bool update changes the lines get redrawn

    #controls how the points of the line get updates
    def update_vals(self,car_pos,diff_pos,rotation):
        #easy trick to move the line the same distance as the car moves
        self.x1+= diff_pos[0]
        self.y1+=diff_pos[1]
        self.x2+= diff_pos[0]
        self.y2+=diff_pos[1]

        self.update_rotation(car_pos,rotation) #updating the rotation of the car

        self.update = True if self.update == False else False #called last to ensure all transformations take place

    #function that controls how the points rotate
    def update_rotation(self,car_pos,rotation):
        x1=self.x1
        y1=self.y1
        x2=self.x2
        y2=self.y2
        origin = car_pos #this pos is defined as the car center
        cx = origin[0] #center x point
        cy = origin[1] #center y point
        angle = rotation #specifying what im using as the angle
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        temp=0
        print('#Rotation# Sin: {} / Cos: {}'.format(sin,cos))

        #code to rotate a point on given origin
        temp = (x1 - cx) * cos - (y1 - cy)* sin + cx
        y1 = (x1 -cx) * sin + (y1 - cy) * cos + cy
        x1 = temp
        #copy and pasted caus lazy
        temp = (x2 - cx) * cos - (y2 - cy)* sin + cx
        y2 = (x2 -cx) * sin + (y2 - cy) * cos + cy
        x2 = temp

        #setting the updated self cordinates values
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    #function thats bound to refence list
    def redraw(self,*args):
        self.the_line.points  = (self.x1,self.y1,self.x2,self.y2)
        print('--REDRAW CALLED--')

    #draws the line with the points x1,y1,x2,y2
    def _draw_line(self):
        with self.canvas:
            Color(rgb=(0,0,1)) #choosing a color
            self.the_line = Line(points=(self.x1,self.y1,self.x2,self.y2),width=4) #creating the line points
