from utlis import *
import cv2

w, h = 640, 480
pid = [0.4, 0.4, 0]
pError = 0
startCounter = 0  # for no Flight 1 - for flight 0

drone = initializeDrone()

while True:

    # Flight
    if startCounter == 0:
        drone.takeoff()
        startCounter = 1

    # Step 1
    img = droneGetFrame(drone, w, h)

    # Step 2
    img, info = faceDetect(img)

    # Step 3
    pError = trackFace(drone, info, w, pid, pError)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break