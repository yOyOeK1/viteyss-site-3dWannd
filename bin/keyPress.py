
from evdev import uinput, ecodes as e
import sys

import time




def setPoint1(ui, x,y,z):
    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
    ui.write(e.EV_KEY, e.KEY_A, 1)
    ui.syn()
    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
    ui.write(e.EV_KEY, e.KEY_A, 0)
    ui.syn()

def setEnter(ui):
   
    ui.write(e.EV_KEY, e.KEY_ENTER, 1)
    ui.syn()
    ui.write(e.EV_KEY, e.KEY_ENTER, 0)
    ui.syn()

   

def setPoint2(ui, x,y,z):

    ui.write(e.EV_KEY, e.KEY_G, 1)
    ui.syn()
    

def setPoint3(ui, x,y,z):

    ui.write(e.EV_KEY, x, 1)
    ui.syn()
    ui.write(e.EV_KEY, x, 0)
    ui.syn()

def setPoint4(ui, x,y,z):

    ui.write(e.EV_KEY, e.KEY_TAB, 1)
    ui.syn()
    ui.write(e.EV_KEY, e.KEY_TAB, 0)
    ui.syn()

def setPoint5(ui, x,y,z):

    ui.write(e.EV_KEY, y, 1)
    ui.syn()
    

def setPoint6(ui, x,y,z):

    ui.write(e.EV_KEY, e.KEY_TAB, 1)
    ui.syn()
    ui.write(e.EV_KEY, e.KEY_TAB, 0)
    ui.syn()

def setPoint7(ui, x,y,z):

    ui.write(e.EV_KEY, z, 1)
    ui.syn()

def setPoint8(ui, x,y,z):

    ui.write(e.EV_KEY, e.KEY_ENTER, 1)
    ui.syn()


def main(args):

    ex = e.KEY_1
    ey = e.KEY_5
    ez = e.KEY_3

    time.sleep(5)
    with uinput.UInput() as ui:
       setPoint1(ui, ex, ey, ez)
    
    time.sleep(.5)
    with uinput.UInput() as ui:
       setEnter(ui)

    time.sleep(.5)
    with uinput.UInput() as ui:
       setPoint2(ui, ex, ey, ez)
    
    time.sleep(.5)
    with uinput.UInput() as ui:
       setPoint3(ui, ex, ey, ez)

    time.sleep(.5)
    with uinput.UInput() as ui:
       setPoint4(ui, ex, ey, ez)

    #time.sleep(.5)
    #with uinput.UInput() as ui:
    #   setPoint5(ui, ex, ey, ez)




if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: {}")
        sys.exit(1)
    main(sys.argv)