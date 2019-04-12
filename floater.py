# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import model

class Floater(Prey):  
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,model.random_angle(),5)
        self._color = 'red'
            
    def update(self,model):
        if random.random() < .3:
            speed = self.get_speed()+.5*random.random()*random.choice([-1,1])
            if speed > 7:
                speed = 7
            if speed < 3:
                speed = 3
            angle = self.get_angle()+.5*random.random()*random.choice([-1,1])
            self.set_velocity(speed,angle)
        self.move()
        self.wall_bounce()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
        