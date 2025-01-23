
plan_de_vol_fr = []
plan_de_vol_en = []

drone_commands = {
    "avant": "forward",
    "arriere": "back",
    "right": "droite",
    "left": "gauche",
    "haut": "up",
    "bas": "down",
    "rotation": "rotate",
    "atterrir": "land",
    "decoller": "takeoff",
    "retourner": "flip"
}

def afficher_plan_vol_fr():
    for p in plan_de_vol_fr:
        if p[0] == "rotation":
            print(f">>> {p[0]} de {p[1]} degrés")
        if p[0] in ["atterrir", "decoller"]:
            print(f">>> {p[0]} [++]")
        elif p[0] == "retourner":
            print(f">> {p[0]} --> {p[1]}")
        else:
            print(f">> {p[0]} --> {p[1]} cm")

def afficher_plan_vol_en():
    for p in plan_de_vol_en:
        if p[0] == "rotate":
            print(f">>> {p[0]} de {p[1]} degrés")
        if p[0] in ["land", "takeoff"]:
            print(f">>> {p[0]} [++]")
        elif p[0] == "flip":
            print(f">> {p[0]} --> {p[1]}")
        else:
            print(f">> {p[0]} --> {p[1]} cm")

def lecture_plan_vol_en():
    cmd_param = ["forward", "back", "up", "down", "left", "right", "rotate", "flip"]
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
                    if cmd == "flip":
                        param = "left"
                    else:
                        param = 10

                if not (cmd in cmd_param or cmd in cmd_no_param):
                    continue

                plan_de_vol_en.append((cmd, param))

    except FileNotFoundError:
        print(f"[ERROR] The File {f_vol} was not found")
        return False

    if len(plan_de_vol_en) > 0:
        return True
    else:
        print(f"[Attention] The {f_vol} is empty")
        return False

def lecture_plan_vol_fr():
    cmd_param = ["avant", "arriere", "haut", "bas", "gauche", "droite", "rotation", "retourner"]
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
                    if cmd == "retourner":
                        param = commande[1]
                    else:
                        param = int(commande[1])
                else:
                    param = None

                if cmd in cmd_no_param:
                    param = None

                if cmd in cmd_param and param == None:
                    if cmd == "retourner":
                        param = "gauche"
                    else:
                        param = 10

                if not (cmd in cmd_param or cmd in cmd_no_param):
                    continue

                plan_de_vol_fr.append((cmd, param))

    except FileNotFoundError:
        print(f"[ERREUR] Le fichier {f_vol} est vide ")
        return False

    if len(plan_de_vol_fr) > 0:
        return True
    else:
        print(f"[Attention] Le fichier {f_vol} est vide")
        return False

def pilotage(drone, plan_vol):
    for c in plan_vol:
        commande = c[0]
        parametre = c[1]

        if commande in ["forward", "avant"]:
            drone.move_forward(parametre)

        elif commande in ["back", "arriere"]:
            drone.move_back(parametre)

        elif commande in ["right", "droite"]:
            drone.move_right(parametre)

        elif commande in ["left", "gauche"]:
            drone.move_left(parametre)

        elif commande in ["up", "haut"]:
            drone.move_up(parametre)

        elif commande in ["down", "bas"]:
            drone.move_down(parametre)

        elif commande in ["rotate", "rotation"]:
            drone.rotate_clockwise(parametre)
        elif commande in ["land", "atterrir"]:
            drone.land()

        elif commande in ["takeoff", "decoller"]:
            drone.takeoff()

        else:
            print("[ERREUR/ERROR] mauvaise commande")