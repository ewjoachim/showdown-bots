

SHOOT, DODGE, RELOAD, STAND, SHOOT_NO_BULLET = range(5)
actions_possibles = ("shoot", "dodge", "reload", "stand", "shoot_no_bullet")
actions_reception = actions_possibles[0:5]
actions_envoie = actions_possibles[0:3]

moi_nb_max_reload = 5
moi_nb_bullet = 1

autre_nb_max_reload = 5
autre_nb_bullet = 1

print("Melissa")

while True:
    print(actions_envoie[DODGE])
    other = input()
    # what's happens

	# SHOOT
    if other == actions_reception[SHOOT]:
	    # comptage pour l'autre
        autre_nb_bullet -= 1

        if autre_nb_bullet == 0 and moi_nb_bullet > 0 :
            print(actions_envoie[SHOOT])
            moi_nb_bullet -= 1
        else:
            print(actions_envoie[RELOAD])
            moi_nb_max_reload -= 1
            moi_nb_bullet += 1

	# DODGE
    elif other == actions_reception[DODGE]:
	    # comptage pour l'autre

        if moi_nb_bullet > 0:
            print(actions_envoie[SHOOT])
            moi_nb_bullet -= 1
        else:
            print(actions_envoie[DODGE])

	# RELOAD
    elif other == actions_reception[RELOAD]:
	    # comptage pour l'autre
        if autre_nb_max_reload > 0:
            autre_nb_max_reload -= 1
            autre_nb_bullet += 1

        if moi_nb_bullet > 0:
            print(actions_envoie[SHOOT])
            moi_nb_bullet -= 1
        else:
            if autre_nb_bullet > 0:
                print(actions_envoie[DODGE])
            else:
                print(actions_envoie[RELOAD])
                moi_nb_max_reload -= 1
                moi_nb_bullet += 1

	# STAND
    elif other == actions_reception[STAND]:
        print(actions_envoie[DODGE])

	# SHOOT_NO_BULLET
    elif other == actions_reception[SHOOT_NO_BULLET]:
        print(actions_envoie[SHOOT])




