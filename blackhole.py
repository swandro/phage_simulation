# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from destroyer import Special
import model

class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._color='black'
    
    def contains(self,xy):
        return self.distance(xy) < self.radius
    
    def update(self,model):
        eaten = set()
        for item in model.find(Prey):
            if self.contains(item.get_location()):
                if type(item)==Special:
                    model.things = set([i for i in model.things if i != self])
                else:
                    model.things = set([i for i in model.things if i != item])
                    eaten.add(item)
        return eaten
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill=self._color)
