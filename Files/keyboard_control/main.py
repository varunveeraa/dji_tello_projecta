from djitellopy import tello
import keyPress as key
from time import sleep

key.init()
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

def getInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    if key.getKey("LEFT"): 
        lr = -50
    elif key.getKey("RIGHT"): 
        lr = 50
    
    if key.getKey("UP"): 
        ud = -50
    elif key.getKey("DOWN"): 
        ud = 50
    
    if key.getKey("w"): 
        fb = -50
    elif key.getKey("s"): 
        fb = 50
    
    if key.getKey("a"): 
        yv = -50
    elif key.getKey("d"): 
        yv = 50
        
    if key.getKey("T"):
        drone.takeoff()
    if key.getKey("L"):
        drone.land()
     
    return [lr, fb, ud, yv]
    


while True:
    val = getInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])
    sleep(0.05)

