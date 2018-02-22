#!/usr/bin/env python
"""
Greetsdlfnj, I'm the Randomizer !
Usage: showdown-example randomizer name
I play randomly shoot, dodge and reload
with equal probability.
"""
import random
import sys

name = "flibidi"

nb_tours = 0
balles_adv = 1
balles_moi = 1
nb_dodge_adv = 0
nb_dodge_moi = 0
action_adv = ""

print(name)

while True:

	action=None
	nb_tours += 1

	if nb_tours == 1:
		action="shoot"

	elif balles_adv == 6:
		action="dodge"

	elif balles_moi == 6:
		action="shoot"

	elif balles_adv == 0:
		action="reload"

	elif (nb_dodge_adv - nb_dodge_moi) > (100 - nb_tours):
		action = "dodge"

	elif balles_adv == 0 and balles_moi > 2:
		action="shoot"

	if action is None and balles_moi > 1:
		action = random.choice("shoot dodge reload".split())

	elif action is None:
		action = random.choice("dodge reload".split())

	if action == "reload":
		balles_moi += 1
	elif action == "shoot":
		balles_moi -= 1
	else:
		nb_dodge_moi += 1

	if nb_tours > 1: action_adv = input()

	if action_adv == "shoot":
		balles_adv -= 1
	elif action_adv == "dodge":
		nb_dodge_adv += 1
	else:
		balles_adv += 1



	print(action)
