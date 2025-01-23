from time import sleep
from djitellopy import Tello
from sys import exit

drone_commands = {
    "avant": "forward",
    "arriere": "back",
    "right": "droite",
    "left": "gauche",
    "haut": "up",
    "bas": "down",
    "rotation": "rotate",
    "atterrir": "land",
    "decoller": "takeoff"
}

plan_de_vol = []
drone = Tello()

def lecture_plan_vol_en():
    cmd_param = ["forward", "back", "up", "down", "left", "right", "rotate"]
    cmd_no_param = ["land", "takeoff"]

    f_vol = "plan_de_vol.txt"
    try:
        with open(f_vol, 'r') as f:
            commandes = f.readlines()

        for commande in commandes:
            if commande != '' and commande != '\n':
                commande = commande.rstrip()
                commande = commande.lstrip()
                commande = commande.split()
                cmd = commande[0]
                if len(commande) >= 2:
                    param = int(commande[1])
                else:
                    param = None

                if cmd in cmd_no_param:
                    param = None

                if cmd in cmd_param and param == None:
                    param = 10

                if not (cmd in cmd_param or cmd in cmd_no_param):
                    continue

                plan_de_vol.append((cmd, param))

    except FileNotFoundError:
        print("[ERREUR] il y a eu erreur lors de la lecture du Fichier")
        return False

    if len(plan_de_vol) > 0:
        return True
    else:
        print("[Attention] Le fichier est vide")
        return False


def lecture_plan_vol_fr():
    cmd_param = ["avant", "arriere", "haut", "bas", "gauche", "droite", "rotation"]
    cmd_no_param = ["atterrir", "decoller"]

    f_vol = "plan_de_vol.txt"
    try:
        with open(f_vol, 'r') as f:
            commandes = f.readlines()

        for commande in commandes:
            if commande != '' and commande != '\n':
                commande = commande.rstrip()
                commande = commande.lstrip()
                commande = commande.split()
                cmd = commande[0]
                if len(commande) >= 2:
                    param = int(commande[1])
                else:
                    param = None

                if cmd in cmd_no_param:
                    param = None

                if cmd in cmd_param and param == None:
                    param = 10

                if not (cmd in cmd_param or cmd in cmd_no_param):
                    continue
                try:
                    cmd_en = drone_commands[cmd]
                    plan_de_vol.append((cmd_en, param))
                except KeyError:
                    print(f"[Erreur] {cmd} n'est pas une commande valide")

    except FileNotFoundError:
        print("[ERREUR] il y a eu erreur lors de la lecture du Fichier")
        return False

    if len(plan_de_vol) > 0:
        return True
    else:
        print("[Attention] Le fichier est vide")
        return False


def pilotage(commande,parametre):

    if commande == "forward":
        drone.move_forward(parametre)

    elif commande == "back":
        drone.move_back(parametre)

    elif commande == "right":
        drone.move_right(parametre)

    elif commande == "left":
        drone.move_left(parametre)

    elif commande == "up":
        drone.move_up(parametre)

    elif commande == "down":
        drone.move_down(parametre)

    elif commande == "rotate":
        drone.rotate_clockwise(parametre)
    elif commande == "land":
        drone.land()

    elif commande == "takeoff":
        drone.takeoff()

    else:
        print("[ERREUR/ERROR] mauvaise commande")

def control():
    for c in plan_de_vol:
        pilotage(c[0], c[1])
        sleep(2)

if __name__ == "__main__":

    print("#### DRONE PLAN DE VOL ####")
    print("---------------------------")

    while True:
        langue = input(">>> Choisissez la langue de votre plan de vol (FR/EN) | Q pour quitter: ")
        if langue.lower() == "fr":
            verification = lecture_plan_vol_fr()
            break
        elif langue.lower() == "en":
            verification = lecture_plan_vol_en()
            break
        elif langue.lower() == "q":
            exit()
        else:
            print("Mauvais choix")

    if verification:
        print(">>> Lecture du plan de vol")
        print("--------------------------\n")
        for p in plan_de_vol:
            if p[0] == "rotate":
                print(f">>> {p[0]} de {p[1]} degrés")
            if p[0] in ["land", "takeoff"]:
                print(f">>> {p[0]} [++]")
            else:
                print(f">> {p[0]} --> {p[1]} cm")

        if plan_de_vol[0][0] != "takeoff":
            print("[+] Votre plan de vol manque l'instruction de décollage")
            t = input("\t>> Voulez-vous ajouté le décollage au plan de vol (Oui/Non) ? ")
            if t.lower() == "oui":
                plan_de_vol.insert(0, ("takeoff", None))

        if plan_de_vol[-1][0] != "land":
            print("[+] Votre plan de vol manque l'instruction d'atterrissage")
            l = input("\t>> Voulez-vous ajouté l'atterrissage au plan de vol (Oui/Non) ? ")
            if l.lower() == "oui":
                plan_de_vol.append(("land", None))

        drone.connect()
        control()

    else:
        print("[ERREUR] Veuillez vérifier le fichier du plan de vol!!")
