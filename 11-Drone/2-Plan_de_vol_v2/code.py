from djitellopy import Tello
from tello_modules import *

def main():
    drone = Tello()
    drone.connect()

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

        if langue.lower() == "fr":
            print(">>> Lecture du plan de vol")
            print("--------------------------\n")

            if plan_de_vol_fr[0][0] != "decoller":
                print("[+] Votre plan de vol manque l'instruction de décollage")
                t = input("\t>> Voulez-vous ajouté le décollage au plan de vol (Oui/Non) ? ")
                if t.lower() == "oui":
                    plan_de_vol_fr.insert(0, ("decoller", None))

            if plan_de_vol_fr[-1][0] != "atterrir":
                print("[+] Votre plan de vol manque l'instruction d'atterrissage")
                l = input("\t>> Voulez-vous ajouté l'atterrissage au plan de vol (Oui/Non) ? ")
                if l.lower() == "oui":
                    plan_de_vol_fr.append(("atterrir", None))

            afficher_plan_vol_fr()
            pilotage(drone, plan_de_vol_fr)

            # Appel
        else:
            print(">>> Printing Flight Path")
            print("--------------------------\n")

            if plan_de_vol_en[0][0] != "takeoff":
                print("[+] Your Flight plan is missing takeoff")
                t = input("\t>> Would you like to takeoff to your flight plan  (Yes/No) ? ")
                if t.lower() == "yes":
                    plan_de_vol_en.insert(0, ("takeoff", None))

            if plan_de_vol_en[-1][0] != "land":
                print("[+] Your Flight plan is missing the landing instruction")
                l = input("\t>> Would you like to add it to the flight plan (Yes/No) ? ")
                if l.lower() == "yes":
                    plan_de_vol_en.append(("land", None))

            afficher_plan_vol_en()
            pilotage(drone, plan_de_vol_en)

    else:
        print("[ERREUR] Veuillez vérifier le fichier du plan de vol!!")

if __name__ == "__main__":
    main()