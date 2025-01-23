from time import sleep
from djitellopy import Tello

def main():
    drone.takeoff()

    for i in range(4):
        drone.move_forward(80)
        sleep(5)
        drone.rotate_clockwise(90)

    print("### Atterissage dans 5 sécondes ###")
    sleep(5)
    drone.land()

if __name__ == '__main__':
    drone = Tello()
    drone.connect()
    main()