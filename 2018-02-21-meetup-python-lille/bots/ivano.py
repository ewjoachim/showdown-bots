# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:20:11 2018

@author: Ivano
"""

import random
import sys

#Send your program name
print("ivano")

#enemy action is input()

n_bullets = 1
my_bullets = 1
actions = {"shoot", "dodge", "reload"}
first_t = True
while True:

    if first_t != True:
        n_prev_action = input()
        round_actions = list(actions) #Copy of possible actions this round
    else:
        n_prev_action = "placeholder"
        print("dodge") #First turn action is dodge

        first_t = False



        #Enemy bullets count/increment
        if n_prev_action == "reload":
            n_bullets += 1
        elif n_prev_action == "shoot":
            n_bullets -= 1
        else:
            pass

        #Removal of "useless" actions
        if n_bullets == 0:
            round_actions.remove("dodge") #If the enemy has no bullets, no need to dodge
        if my_bullets == 0:
            round_actions.remove("shoot") #If I have no bullets, I can't shoot
        elif my_bullets > 6:
            round_actions.remove("reload") #If my clip is full, no need to reload

        round_action = random.choice(round_actions)


        #My bullets incremenet/decrement
        if round_action == "reload" and my_bullets < 7:
            my_bullets = my_bullets +1
        elif round_action == "shoot" and my_bullets > 0:
            my_bullets -=1
        else:
            pass

        print(round_action)


