import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
import math,random
from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from destroyer import Special
from bacteria import Bacteria
from phage import Phage


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
things       = set()
selected = 'Ball'

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls,things
    running     = False
    cycle_count = 0
    things       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just 1 update in the simulation
def step ():
    global running
    running=True
    update_all()
    display_all()
    running=False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected
    selected = str(kind)


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if selected=='Remove':
        to_remove=None
        for item in things:
            if item.contains((x,y)):
                to_remove = item
        remove(to_remove)
    else:
        add(eval(selected+'('+str(x)+','+str(y)+')'))


#add simulton s to the simulation
def add(s):
    global things
    things.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global things
    if s != None:
        things.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for item in things:
        if isinstance(item,p):
            result.add(item)
    return result

#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in things:
            b.update(model)


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in things:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(things))+" balls/"+str(cycle_count)+" cycles")

def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2


def random_color():
    # hex(52) -> "0x34", so [2:] is the two hex digits, without the 0x prefix
    return "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]

def random_speed():
    # Magnitude is 5-10
    return random.randint(5,10)
