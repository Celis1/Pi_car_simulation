from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty,
    ObjectProperty,ListProperty)
from random import randint
from Sensor_class import Sensor
Builder.load_file('Styles/SensorManager.kv')

class SensorManager(Widget):
#creating the velocity variables
    ''' Creating the sensor manager that controls all the
    sensors and updates their rotation based on the car_img
    --
    car_obj: the car widget the lines have to follow
    line_list: list of 4 values x1,y1,x2,y2 '''

    sensor_angle = NumericProperty(0)
    # ... now needs a list of sensors

    def __init__(self,car_obj,**kwargs):
        super(SensorManager,self).__init__(**kwargs)
        #self.line_list = line_list #edited line list
        self.pos = car_obj.center #setting manager widget as the cars center

        #making the variables needed later for editing
        self.car_pos = car_obj.pos #making it easier to have the car position
        self.car_vel = car_obj.velocity #making it easier to have to car velocity
        self.car_angle = car_obj.angle #the total angle of rotation
        self.car_rotation = car_obj.rotation #the incoming angle to rotate

        self._create_sensors() #creating all the sensors  ... later need to add json parameter

    #this is only to keep the sensor_mangers position and to call on the sensors update values
    def move(self,car_pos,rotation,diff_pos):
        self.pos = car_pos #keeping the sensor_manager centered on the cars center (in main file the car center is being passed through the move)
        #updating the value of the sensor ...make for multiple sensors
        self.test_sense.update_vals(car_pos,diff_pos,rotation) #testing updating the line values
        #self._print_values() #debugging
        self.test2.update_vals(car_pos,diff_pos,rotation)

    #adding the sensor widgets to the parent sensor manager
    def _create_sensors(self):
        test_vals = (910,310,1000,400) #test for creating 1 line
        self.test_sense = Sensor(test_vals,self.car_pos) #creating a test sensor
        self.add_widget(self.test_sense)
        test2_vals = (910,190,1000,90)
        self.test2 = Sensor(test2_vals,self.car_pos)
        self.add_widget(self.test2)

    def _print_values(self): #all the print statements
        print('###line_manger_Pos#',self.pos)
        print('Cars current angle:',self.car_angle)
        print('cars_pos?###',self.car_pos)
        print('cars_velocity?###',self.car_vel)
        print('cars incoming angle of adjustment###',self.car_rotation)
