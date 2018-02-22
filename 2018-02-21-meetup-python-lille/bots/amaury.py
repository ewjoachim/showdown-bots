#import
import random

#debug mode /!\ -> turn Flase for your own safety during real use
debug = True

#initialization => has to be set up by Player
botname = "Bobot"
shoot_first_turn_probability = 50

#debug information and parameters
bullet = 1
opponnent_bullet = 1
turn = 0
player_actions = []
opponnent_actions = []
dice = random.randint(1,100)
game = True
player = True
opponnent = True

#actions
action_shoot = "shoot"
action_dodge = "dodge"
action_reload = "reload"

def start():
    print(botname)
    if (dice > shoot_first_turn_probability):
        print(action_shoot)
    else:
        print(action_dodge)
    global turn
    turn = 1

    func_debug_info

def main():

    global game
    global opponnent_bullet
    global opponnent_actions
    global player_actions
    while game == True:

        oppennent_action = input()
        if debug:
            #debug loop
            if (oppennent_action == "!exit") | (player == False) | (opponnent == False):
                game = False
            else:
                #begin of game
                player_action(oppennent_action,opponnent_bullet)
                #end of game

            #print statistics
            func_debug_info
        else:
            player_action(oppennent_action,opponnent_bullet)
    func_stop

#player action
def player_action(oppennent_action,opponnent_bullet):

    #    Using a dictionnary
#    {
#         "shoot": func_op_shoot,
#         "dodge": func_op_dodge,
#         "reload": func_op_reload
#
#    }.get(action, func_default)(action)

    opponnent_actions.append(oppennent_action)
    global turn
    turn = turn + 1

    if opponnent_bullet >= 1:
        if ((oppennent_action == action_dodge) & (opponnent_actions[-1] == action_dodge) & bullet != 0):
            func_op_shoot(oppennent_action)
        elif bullet >= 1:
            if oppennent_action == action_shoot:
                opponnent_bullet = opponnent_bullet + 1
                func_op_reload(oppennent_action)
            elif oppennent_action == action_dodge:
                func_op_shoot(oppennent_action)
            elif oppennent_action == action_reload:
                opponnent_bullet = opponnent_bullet + 1
                func_op_dodge(oppennent_action)
            else:
                func_op_shoot(oppennent_action)
        elif ((bullet == 0) & (opponnent_actions[-1] == action_dodge) & (opponnent_bullet == 0 )):
            func_op_reload(oppennent_action)
        elif ((bullet == 0) & (opponnent_actions[-1] == action_dodge) & (opponnent_bullet >= 1 )):
            func_op_dodge(oppennent_action)
        elif ((oppennent_action == action_dodge) & (opponnent_actions[-1] == action_reload) & bullet != 0):
            func_op_shoot(oppennent_action)
        else:
            func_op_reload(oppennent_action)
    elif bullet == 0:
        if ((oppennent_action == action_shoot) & (opponnent_actions[-1] == action_dodge) & (opponnent_bullet <= 1 )):
            func_op_reload(oppennent_action)
    else:
        func_op_shoot(oppennent_action)

def func_op_shoot(opponent_action):
    player_action = print(action_shoot)
    player_action
    player_actions.append(player_action)
    global bullet
    bullet = bullet-1

def func_op_dodge(opponent_action):
    player_action = print(action_dodge)
    player_action
    player_actions.append(player_action)

def func_op_reload(opponent_action):
    player_action = print(action_reload)
    player_action
    player_actions.append(player_action)
    global bullet
    bullet = bullet+1

def func_debug_info():
    print(turn)
    print(bullet)
    print(opponnent_bullet)
    print(len(opponnent_actions))
    print(opponnent_actions.count(action_shoot))
    print(opponnent_actions.count(action_reload))
    print(opponnent_actions.count(action_dodge))
    print(player_actions)
    print(opponnent_actions)

def func_stop(opponnent_action):
    raise Exception('exit')

def func_oppennent_bullet(oppennent_bullet):
    if (oppennent_bullet == 6):
        print(action_dodge)
    elif (oppennent_bullet == 0):
        print(action_shoot)
    else:
        print(action_reload)

start()
main()
