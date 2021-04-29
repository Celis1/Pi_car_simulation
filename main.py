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


#from Car import Car
from Sensor_manager import SensorManager
from Paint_widget import MyPaintWidget
#testing
#from old_files.Sensor_manager_old import SensorManager
from Brain.ai import get_action
from Car import Bot
Builder.load_file('Styles/main.kv')


#creating widgets to track canvas origin (DEBUGGING only)
class Origin_plot(Widget):
    #creates a new widget every time instead of drawing another circle
    #will greatly reduce frames after a couple hundred instantiantions
    def __init__(self,gin_x,gin_y,clr, **kwargs):
        super(Origin_plot,self).__init__(**kwargs)
        with self.canvas.after:
            Color(rgb=clr)
            Ellipse(pos=(gin_x,gin_y),size=(15,15))

class GameScreen(Widget):
    ''' Creating the GameScreen Widget, every other widget should be in
    this class '''
    test_angle = NumericProperty(0) # for debbugigng

    def on_start(self):
        ''' first function run when game boots '''
        print('###starting up###') #lol
        self.my_bot = Bot() #instantiating the car object
        self.add_widget(self.my_bot) #adding the widget to the screen
        self.add_widget(Origin_plot(self.my_bot.pos[0],self.my_bot.pos[1],(1,0,0))) #creating an origin point
        self.my_bot.start() #calling the bots start method

        #creating the sensor manager
        self.my_sensor_manager = SensorManager(self.my_bot)#instantiating the Sensor Manager which takes in a bot
        self.add_widget(self.my_sensor_manager) #adding the Sensors to the screen

    #controls all actions taken every frame
    def update(self,dt):
        self.test_angle = randint(-90,90) #creating random angle
        #self.test_angle=5

        self.my_bot.move(self.test_angle)

        #updating the sensor Object
        self.my_sensor_manager.move(self.my_bot.center,self.my_bot.rotation,self.my_bot.the_diff)

        #self.my_bot.other_move(some_angle)
        self.add_widget(Origin_plot(self.my_bot.pos[0],self.my_bot.pos[1],(.5,.5,.8)))

        #sensor manager plotter
        #self.add_widget(Origin_plot(self.my_sensor_manager.test_sense.x1,self.my_sensor_manager.test_sense.y1,(0,1,0)))

#Creating the Kivy App, build is called on run
class CarApp(App):
    def build(self):
        self.game = GameScreen()
        self.game.on_start()

        self.painter = MyPaintWidget()
        self.game.add_widget(self.painter) #... creating paint widget

        Clock.schedule_interval(self.game.update,.1) #everyframe the update function is called

        return self.game

if __name__ == '__main__':
    CarApp().run()
