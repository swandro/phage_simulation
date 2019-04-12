# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import model

class Hunter(Pulsator,Mobile_Simulton):
    view_distance = 200
    
    def __init__(self,x,y):
        Mobile_Simulton.__init__(self,x,y,20,20,model.random_angle(),5)
        self._color='black'
        self.counter = 30
    
    def update(self,model):
        Pulsator.update(self,model)
        self.move()
        self.wall_bounce()
        prey_nearby = False
        nearest_distance = Hunter.view_distance
        for item in model.find(Prey):
            dist = self.distance(item.get_location())
            if dist < Hunter.view_distance and dist < nearest_distance:
                nearest = item
                nearest_distance = dist
                prey_nearby = True
        if prey_nearby:
            self._angle = atan2(-(self._y-nearest._y),-(self._x-nearest._x))
