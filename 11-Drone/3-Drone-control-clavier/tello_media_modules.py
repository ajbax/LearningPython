import cv2
from time import sleep, strftime

keepRecording = False

def videoTello(drone):
    global keepRecording

    if keepRecording:
        exit()
    keepRecording = True

    drone.streamon()
    sleep(5)
    frame_read = drone.get_frame_read()
    height, width, _ = frame_read.frame.shape
    timestr = strftime("%Y%m%d-%H%M%S")
    fichier_video = f"videos/drone-video-{timestr}.avi"
    video = cv2.VideoWriter(fichier_video, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        sleep(1 / 30)

    video.release()
    drone.streamoff()
    keepRecording = False

def photoTello(drone):
    global keepRecording

    if keepRecording:
        print("Arrêt de l'enregistrement vidéo en cours ...")
        keepRecording = False
        sleep(2)

    drone.streamon()
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 260))
    cv2.imshow("Tello Photo", img)
    cv2.waitKey(1)
    timestr = strftime("%Y%m%d-%H%M%S")
    fichier_image = f"images/image{timestr}.jpg"
    cv2.imwrite(fichier_image, img, [cv2.IMWRITE_JPEG_QUALITY, 100])