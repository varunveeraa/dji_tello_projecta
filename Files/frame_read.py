from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.streamon()

while True:
    frame = drone.get_frame_read().frame
    #frame = cv2.resize(frame, (720, 480))
    cv2.imshow("Live Stream", frame)
    cv2.waitKey(1)
    
