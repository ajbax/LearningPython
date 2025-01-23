import cv2
import time
from threading import Thread
from djitellopy import Tello

drone = Tello()
drone.connect()

keepRecording = True
drone.streamon()
frame_read = drone.get_frame_read()

def videoRecorder():
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('videos/drone-video-boreal.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)
    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()

drone.takeoff()
drone.move_up(80)
time.sleep(2)
drone.rotate_counter_clockwise(360)
time.sleep(2)
drone.land()

keepRecording = False

recorder.join()