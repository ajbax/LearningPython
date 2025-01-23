import cv2
from djitellopy import Tello

from time import strftime, sleep

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_up(30)

for i in range(4):
    timestr = strftime("%Y%m%d-%H%M%S")
    cv2.imwrite(f"picture-{timestr}.png", frame_read.frame)
    sleep(3)
    tello.rotate_clockwise(90)


tello.land()