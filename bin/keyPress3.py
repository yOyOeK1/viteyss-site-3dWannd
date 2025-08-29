import uinput as u
import time 
from threading import Thread

NoToConst = {
    '-' : u.KEY_APOSTROPHE,
    '.': u.KEY_E,
    '0': u.KEY_0, '4': u.KEY_4, '9': u.KEY_9,
    '1': u.KEY_1, '5': u.KEY_5, '8': u.KEY_8,
    '2': u.KEY_2, '6': u.KEY_6, 
    '3': u.KEY_3, '7': u.KEY_7
}


def doNumburToKeysStroke( device, numb ):
    global NoToConst
    strToPunch = f"{numb}"
    for c in strToPunch:
        device.emit_click( NoToConst[ c ] )
        time.sleep(.01)




def setXYZPOI( device, x, y, z ):
    print("go ")
    #with u.Device([ u.KEY_LEFTSHIFT, u.KEY_A, u.KEY_ENTER, u.KEY_U, u.KEY_G, u.KEY_TAB,
    #    u.KEY_0, u.KEY_1, u.KEY_2, u.KEY_3, u.KEY_4, u.KEY_5, u.KEY_6, u.KEY_7,
    #    u.KEY_8, u.KEY_9, u.KEY_COMMA, u.KEY_MINUS, u.KEY_V,
    #    u.KEY_E,u.KEY_APOSTROPHE  ]) as device:

    #    time.sleep(.2)

    #doNumburToKeysStroke(device, -1.0432)

    #exit(1)


    device.emit(u.KEY_LEFTSHIFT,    1)
    device.emit_click(u.KEY_A)
    device.emit(u.KEY_LEFTSHIFT,    0)


    tDelay = 0.2

    time.sleep(tDelay)
    device.emit(u.KEY_ENTER, 1)
    time.sleep(tDelay)
    device.emit(u.KEY_ENTER, 0)

    time.sleep(tDelay)
    device.emit_click(u.KEY_U) # G

    time.sleep(tDelay)
    # set x
    #device.emit_click(u.KEY_1)
    doNumburToKeysStroke(device, x)

    time.sleep(tDelay)
    device.emit_click(u.KEY_TAB)

    time.sleep(tDelay)
    # set y
    #device.emit_click(u.KEY_2)
    doNumburToKeysStroke(device, y)

    time.sleep(tDelay)
    device.emit_click(u.KEY_TAB)

    time.sleep(tDelay)
    #set x
    #device.emit_click(u.KEY_0)
    doNumburToKeysStroke(device, z)

    time.sleep(tDelay)
    device.emit(u.KEY_ENTER, 1)
    time.sleep(tDelay)
    device.emit(u.KEY_ENTER, 0)

    #time.sleep(tDelay)


def initDevice():
    return u.Device([ u.KEY_LEFTSHIFT, u.KEY_A, u.KEY_ENTER, u.KEY_U, u.KEY_G, u.KEY_TAB,
            u.KEY_0, u.KEY_1, u.KEY_2, u.KEY_3, u.KEY_4, u.KEY_5, u.KEY_6, u.KEY_7,
            u.KEY_8, u.KEY_9, u.KEY_COMMA, u.KEY_MINUS, u.KEY_V,
            u.KEY_E,u.KEY_APOSTROPHE  ])


devi = initDevice()
def keyPress3( x, y, z, cbOnDone = -1, argsToCb = -1):
    global devi
    
    def run(*args):

        print("threed start")
        time.sleep(.3)
        print("threed sleep")
        #fftime.sleep(5.3)
        setXYZPOI( devi, x,y,z )
        print(["threed end",x,y,z])
        if cbOnDone != -1:
            cbOnDone( argsToCb )

    Thread( target=run).start()
    

if __name__ == "__main__":

    import math
    time.sleep(3)

    device = initDevice()

    time.sleep(.5)

    for i in range(0,2):
        #setXYZPOI(  x,y,z )
        setXYZPOI( device, 10.0+ math.sin(i/3.00)*4.0, 20+math.cos(i/3.00)*4.0 , i*i*0.1 )