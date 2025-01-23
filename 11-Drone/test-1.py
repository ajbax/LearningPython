from random import choice
choix = ["Papier", "Pierre", "Sciseaux"]

cpu = choice(choix)
while True:
    user = input("Faites votre choix {Papier, Pierre, Sciseaux: ")
    if user not in choix:
        print("Entree incorrecte")
    else:
        break

if user == "Papier":
    if cpu == "Sciseaux":
        print(f"CPU gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    elif cpu == "Pierre":
        print("User Gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    else:
        print("egalité")
        print(f"CPU: {cpu} et USER: {user}")
elif user == "Pierre":
    if cpu == "Sciseaux":
        print(f"User gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    elif cpu == "Papier":
        print("User Gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    else:
        print("egalité")
        print(f"CPU: {cpu} et USER: {user}")

else:
    if cpu == "Papier":
        print(f"User gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    elif cpu == "Pierre":
        print("CPU Gagner!!!")
        print(f"CPU: {cpu} et USER: {user}")
    else:
        print("egalité")
        print(f"CPU: {cpu} et USER: {user}")


