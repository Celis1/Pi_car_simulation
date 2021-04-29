from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty,
    ObjectProperty,ListProperty,StringProperty)
from kivy.vector import Vector
from kivy.graphics import *


''' Creating the Car widget this gives the car momentum and rotation'''
class Bot(Widget):
    '''this class caintain the
    --
    velocity: tuple
    angle:float
    rotation:float #this is
    pos:tuple '''

    #creating the velocity variables
    angle = NumericProperty(0)
    rotation=NumericProperty(0) #the angle of rotation passed as a parameter to the move function

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    diff_x = NumericProperty(0) #only used to move the sensor points based on the difference
    diff_y = NumericProperty(0) #only used to move the sensor points based on the difference
    the_diff = ReferenceListProperty(diff_x,diff_y)


    def __init__(self, **kwargs):
        super(Bot,self).__init__(**kwargs)
        self.pos = 800,200 #creating its position
        self.frame_counter = 0 #keeping tracks of the frames for debugging
        self._create_car() #calling its own function
        self.bind(pos=self.update_car) #creating a callback event if the pos changes the function will be called

    #Fist function that should be called
    def start(self):
        self.velocity = Vector(7, 0) #giving the car initial speed
        pass


    #Updates the canvas and its properties
    def update_car(self,*args):
        self.diff_x = self.pos[0]- self.the_car.pos[0] #getting the diffrence of its last x and its current y
        self.diff_y = self.pos[1] - self.the_car.pos[1] #getting the difference of its last y and current y
        #print(self.the_car.pos,self.pos,'car_pos / actual pos')
        #print('test values fo sub [xy]',self.diff_x,self.diff_y)
        self.the_car.pos = self.pos #this updates the new car position linked with bind

    #action taken at every step
    def move(self,rotation):
        self.pos = Vector(*self.velocity).rotate((self.angle)%360) + self.pos
        self.rotation = rotation # getting the rotation of the car
        self.angle = self.angle + self.rotation # updating the angle

    #instantiating the car canvas properties
    def _create_car(self):
        with self.canvas.before: #using canvas to draw
            Color(rgb=(0,1,1))
            self.the_car=Rectangle(pos=self.pos,size=self.size) #creating rect


    #--debugging--
    def _print_values(self):
        ''' creating print values to measure the position of
        the Car, Sensors, and angle '''

        print('####### {} #######'.format(self.frame_counter))
        print('angle position',self.angle)
        print('velocity position',self.velocity_x,self.velocity_y)
        print('bot position:',self.pos)
        #print('car pos:',self.my_car.pos)
        #print('sensor pos:',self.my_sensor_manager.pos)
        self.frame_counter+=1
