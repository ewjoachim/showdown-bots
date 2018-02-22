#!/usr/bin/env python
"""
$
"""
import sys
nombre_de_balle_boot_actuelle = 1
nombre_de_balle_boot_reload = 5
nombre_de_balle_adversaire_actuelle = 1
nombre_de_balle_adversaire_reload = 5

print("Sophie")
ok = set("shoot dodge reload".split())
their_action = "dodge"
tour = 0
c = input()
while (True):
    if ( c == "shoot"):
            if (nombre_de_balle_adversaire_actuelle>0):
                nombre_de_balle_adversaire_actuelle-=1

            if ( nombre_de_balle_adversaire_actuelle == 0):
                their_action = "shoot"

            if ( nombre_de_balle_adversaire_actuelle != 0):
                their_action = "dodge"

    elif (c == "reload"):
            if (nombre_de_balle_adversaire_reload> 0):
                nombre_de_balle_adversaire_actuelle +=1
                nombre_de_balle_adversaire_reload -=1

            if (nombre_de_balle_adversaire_actuelle == 0):
                if (nombre_de_balle_boot_actuelle == 0):
                    their_action = "reload"
                else:
                    their_action = "shoot"
            else:
                    their_action = "dodge"
    elif (c == "shoot_no_bullet"):
        while(True):
            if (nombre_de_balle_boot_actuelle == 0):
                their_action = "reload"
            else:
                their_action = "shoot"
    elif ( c == "stand"):
        if (nombre_de_balle_boot_actuelle == 0):
                their_action = "reload"
        else:
                their_action = "dodge"
    elif ( tour >= 96):
        if (nombre_de_balle_boot_actuelle == 0):
                their_action = "reload"
        else:
                their_action = "shoot"
    else:
        their_action = "dodge"
    tour +=1
    print(their_action)
    if (their_action == "reload"):
        if (nombre_de_balle_boot_reload>0):
            nombre_de_balle_boot_reload-=1
            nombre_de_balle_boot_actuelle+=1
    elif (their_action == "shot"):
            if (nombre_de_balle_boot_actuelle>0):
                nombre_de_balle_boot_actuelle-=1
    c = input()





