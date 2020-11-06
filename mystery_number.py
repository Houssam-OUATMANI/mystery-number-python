# Modules
from math import floor
from random import seed
from random import random

# Variables
essaies = 3
tofind = floor(random() *11)
front_raw = input("Enter a number\n")
front =  int(front_raw)

while (front != tofind and essaies > 0):
    essaies = essaies - 1
    if (essaies == 0):
        print("Il ne vous reste plud d'essais\nPartie terminée")
        break
    if (front > tofind):
        print("Trop grand Veuillez réessayer\nReste " +str(essaies) + " essaies")
    else :
        print("Trop petit Veuillez réessayer\nReste " + str(essaies) + " essaies")
    front_raw = input("Enter a number\n")
    front = int(front_raw)

if (front == tofind):
    print("Bravo tu as gagné\nEffectivement le muméro mystere à deviner est bien le " + str(tofind))
else:
    print("Perdu le muméro mystere à deviner est bien le " + str(tofind))
