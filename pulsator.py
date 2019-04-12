# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from simulton import Simulton
from prey import Prey

class Pulsator(Black_Hole):
    counter = 30
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._color='black'
        self.counter = 30
        
    def update(self,model):
        eaten = Black_Hole.update(self,model)
        if eaten != set():     
            self.change_dimension(1, 1)
            self.counter = 30
        else:
            self.counter -= 1
        if self.counter == 0:
            if self.get_dimension()[0] == 0:
                model.things = set([i for i in model.things if i != self])
            else:
                self.change_dimension(-1, -1)
                self.counter = 30
        self.radius = self.get_dimension()[0]/2
        return eaten