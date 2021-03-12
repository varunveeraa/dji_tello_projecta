from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

print(drone.get_battery())
print(drone.get_attitude())


drone.takeoff()
drone.send_rc_control(0,50,0,0)
sleep(2)
drone.send_rc_control(0,-50,0,0)
sleep(2)
drone.land()

