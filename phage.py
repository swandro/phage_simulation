
from mobilesimulton import Mobile_Simulton
import model
import math,random

class Phage(Mobile_Simulton):
    radius = 5
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,10,10,random.random()*math.pi*2,5)
        self._color = 'orange'
        self._burst_size = 5
        self._replication_time = 10
        self._infection_color = "green"
            
    def update(self,model):
        self.move()
        self.wall_bounce()


    def display(self,canvas):
        canvas.create_oval(self._x-Phage.radius      , self._y-Phage.radius,
                                self._x+Phage.radius, self._y+Phage.radius,
                                fill=self._color)
    
    def get_burst_size(self):
        return self._burst_size
    
    def get_replication_time(self):
        return self._replication_time

    def get_infection_color(self):
        return self._infection_color


