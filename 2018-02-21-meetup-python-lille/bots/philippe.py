print ('philippe')

chargeur_adverse = 1
mon_chargeur = 1
must_shoot = False
prob_shoot_adverse = True

while True:
	
	if (must_shoot == True):
		if (mon_chargeur > 0):
			action = 'shoot'
			mon_chargeur = max(0, mon_chargeur - 1)
		else:
			action = 'reload'
			mon_chargeur += 1
	else:
		if (prob_shoot_adverse == True):
			if (mon_chargeur > 1):
				action = 'shoot'
				mon_chargeur = max(0, mon_chargeur - 1)
			else:	
				action = 'dodge'
		else:
			if (mon_chargeur > 0):
				action = 'shoot'
				mon_chargeur = max(0, mon_chargeur - 1)
			else:	
				action = 'reload'
				mon_chargeur += 1

	print (action)
	action_adverse = input()

	if (action_adverse == 'shoot'):
		chargeur_adverse = max(0, chargeur_adverse - 1)
		if (chargeur_adverse == 0):
			prob_shoot_adverse = False
			must_shoot = True
		else:
			prob_shoot_adverse = True
			must_shoot = False

	if (action_adverse == 'reload'):
		chargeur_adverse += 1
		prob_shoot_adverse = True
		must_shoot = False

	if (action_adverse == 'dodge'):
		if (chargeur_adverse > 0):
			prob_shoot_adverse = True
			must_shoot = False
		else:
			prob_shoot_adverse = False
			must_shoot = True

	if (action_adverse == 'shoot_no_bullet'):
		chargeur_adverse = 0
		must_shoot = True
		prob_shoot_adverse = False

	if (action_adverse == 'stand'):
		must_shoot = True
		prob_shoot_adverse = False
