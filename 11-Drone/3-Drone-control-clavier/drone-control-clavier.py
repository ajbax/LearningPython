from djitellopy import tello
import pygame
from sys import exit
from threading import Thread
from tello_media_modules import *

drone = tello.Tello()
vitesse_drone = 30

try:
    drone.connect()
except Exception as e:
    print(f">> Probleme de connection")
    print(e)
    exit()
t_video = Thread(target=videoTello, args=(drone,))

droneBatteryLevel = drone.get_battery()
print(f">>> Niveau de Batterie: {droneBatteryLevel}")

if droneBatteryLevel <= 5:
    print(f">>> Le niveau de la Batterie est faible: {droneBatteryLevel} %")

    exit()

def init_pygame():
    # Initialisation du module Pygame
    pygame.init()
    global screenSize, screen, clock, droneControl

    # Creation de l'ecran de la taille 1816 x 1069
    screenSize = (723, 468)
    screen = pygame.display.set_mode(screenSize)
    clock = pygame.time.Clock()

    droneControl = True
    controlCommand = False

def main():
    global droneControl, t_video, keepRecording, vitesse_drone

    afficherBatterie = False
    init_pygame()

    while droneControl:
        # Modification de la couleur de fond
        couleurRGB = (255, 255, 255) # de 0 - 255 (Rouge, Vert, Bleu)
        screen.fill(couleurRGB)

        # Ajouter une image de fond
        bgImage = pygame.image.load('img/drone-project.png').convert()
        screen.blit(bgImage, (0, 0))

        pygame.display.set_caption("INF-1093: Projet Drone - Demo")
        test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Le Drone va atterrir")
                drone.land()
                droneControl = False

            if droneControl:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_t:
                        drone.takeoff()

                    if event.key == pygame.K_l:
                        drone.land()

                    if event.key == pygame.K_a:
                        drone.move_forward(vitesse_drone)

                    if event.key == pygame.K_s:
                        drone.move_back(vitesse_drone)

                    if event.key == pygame.K_r:
                        drone.rotate_clockwise(30)

                    if event.key == pygame.K_e:
                        drone.rotate_counter_clockwise(30)

                    if event.key == pygame.K_p:
                        photoTello(drone)

                    if event.key == pygame.K_v:
                        t_video.start()

                    if event.key == pygame.K_g:
                        if vitesse_drone <= 70:
                            vitesse_drone += 10
                            print(f"Nouvelle vitesse est: {vitesse_drone}")
                        else:
                            print(f"Vitesse Max!!! {vitesse_drone}")

                    if event.key == pygame.K_o:
                        if vitesse_drone >= 20:
                            vitesse_drone -= 10
                            print(f"Nouvelle vitesse est: {vitesse_drone}")
                        else:
                            print(f"Vitesse Min!!! {vitesse_drone}")

                    if event.key == pygame.K_LEFT:
                        drone.move_left(vitesse_drone)

                    if event.key == pygame.K_RIGHT:
                        drone.move_right(vitesse_drone)

                    if event.key == pygame.K_DOWN:
                        drone.move_down(vitesse_drone)

                    if event.key == pygame.K_UP:
                        drone.move_up(vitesse_drone)

                    if event.key == pygame.K_ESCAPE:
                        if t_video.is_alive():
                            print("[+] Arrêt de l'enregistrement vidéo...")
                            keepRecording = False
                        afficherBatterie = False

                    if event.key == pygame.K_b:
                        afficherBatterie = True

        if afficherBatterie:
            batterie = drone.get_battery()
            instruction_surf = test_font.render(f'Batterie {batterie}%', False, (51, 227, 255))
            instruction_rect = instruction_surf.get_rect(center=(334, 75))
            screen.blit(instruction_surf, instruction_rect)
            sleep(2)

        pygame.display.update()
        clock.tick(10)

    if t_video.is_alive():
        t_video.join()
    return

if __name__ == "__main__":
    main()