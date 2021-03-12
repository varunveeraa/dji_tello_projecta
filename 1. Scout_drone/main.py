from djitellopy import tello
import keyPress as key
import time
import cv2 

key.init()

drone = tello.Tello()
drone.connect()
drone.streamon()

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
        
    if key.getKey("c"):
        cv2.imwrite(f'Media/Photos/{time.time()}.jpg',frm)
        time.sleep(0.3)
     
    return [lr, fb, ud, yv]
    
while True:
    val = getInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])
    frm = drone.get_frame_read().frame
    frm = cv2.resize(frm, (720, 480))
    cv2.imshow("Live Stream", frm)
    cv2.waitKey(1)