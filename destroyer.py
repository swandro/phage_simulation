from ball import Ball

#This is a special kind of prey that destroys any black hole, pulsar, hunter it comes in contact with



class Special(Ball):
    def __init__(self,x,y):
        Ball.__init__(self,x,y)
        self._color = 'pink'
