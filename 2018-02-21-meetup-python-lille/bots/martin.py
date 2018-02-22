import random

print("Martin-Bot")

global my_nb_bullets
global enemy_nb_bullets

def shoot():
    global my_nb_bullets
    my_nb_bullets -= 1
    print("shoot")

def reload():
    global my_nb_bullets
    my_nb_bullets += 1
    print("reload")

def dodge():
    print("dodge")


if __name__=='__main__':
    global enemy_nb_bullets, my_nb_bullets
    my_nb_bullets, enemy_nb_bullets = 1, 1

    moves = []
    
    while True:

        if enemy_nb_bullets !=0 and my_nb_bullets != 0:
            shoot()
        elif enemy_nb_bullets == 0 and my_nb_bullets == 0:
            reload()
        elif enemy_nb_bullets == 0:
            # Version 1:
            # - Si il y a pas besoin de reload, on force le shoot.
            # - Sinon, soit on shoot, soit on reload.
            if my_nb_bullets == 6:
                shoot()
            else:
                if (random.randint(0,1)==0):
                    reload() # we can reload safely
                else:
                    shoot()
        else:
            dodge()

        move = input()
        moves.append(move)
        if (move=='shoot'):
            enemy_nb_bullets -= 1
        elif (move=='reload'):
            enemy_nb_bullets += 1



            
            
