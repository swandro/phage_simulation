#Bacteria is a subclass of Prey. It can be infected by phage

from prey import Prey
import random,math
import model
from phage import Phage

class Bacteria(Prey):
    radius = 10
    def __init__(self,x,y):
        Prey.__init__(self,x,y,20,20,random.random()*math.pi*2,5)
        self._color = 'yellow'
        self._infected = False
            
    def update(self,model):
        self.move()
        self.wall_bounce()
        if not self._infected:
            for item in model.find(Phage):
                if self.contains(item.get_location()):
                    model.things = set([i for i in model.things if i != item])
                    self.infected(item)
        if self._infected:
            if self._infection_timer == 0:
                self.lyse()
            else:
                self._infection_timer -= 1


    def display(self,canvas):
        canvas.create_oval(self._x-Bacteria.radius      , self._y-Bacteria.radius,
                                self._x+Bacteria.radius, self._y+Bacteria.radius,
                                fill=self._color)
    
    def infected(self, phage):
        self._infected = True
        self._infection_timer = phage.get_replication_time()
        self._burst_size = phage.get_burst_size()
        self._color = phage.get_infection_color()
    
    def lyse(self):
        model.things = set([i for i in model.things if i != self])
        for i in range(self._burst_size):
            model.add(Phage(self.get_location()[0], self.get_location()[1]))