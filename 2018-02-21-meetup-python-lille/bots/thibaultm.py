
import random

class Joueur:
    def __init__(self):
        self.list_coup_prev = []
        self.nb_balle = 1
        self.nb_dodge = 0
        self.name = "No_name"


class etat_game:
    def __init__(self):
        self.Joueur_moi = Joueur()
        self.Joueur_adv = Joueur()
        self.tour = 1
        self.state = "game"

    def _print(self):
        print("Mois, dodge, list, nb_balle,nb_dodge")
        print(self.Joueur_moi.list_coup_prev)
        print(self.Joueur_moi.nb_balle)
        print(self.Joueur_moi.nb_dodge)
        print("Adv, dodge, list, nb_balle,nb_dodge")
        print(self.Joueur_adv.list_coup_prev)
        print(self.Joueur_adv.nb_balle)
        print(self.Joueur_adv.nb_dodge)
        print("Tour")
        print(self.tour)


def main() :
    name="Thibault"
    print(name)
    mesballe=1
    sesballe=1
    i=0
    li=[]
    while i<100 :
        """
        if i==0:
            shoot()
        else :
            random_num=random.random()
            if random_num<1.0/3.0 and mesballe>0 :
                shoot()
            else :
                reload()
        """
        if i%2==0:
            shoot()
        else :
            reload()
        i+=1
        adv=input()
        if adv=="reload":
            sesballe+=1
        if adv=="shoot":
            sesballe-=1
        li.append(adv)

def dodge():
    print("dodge")

def reload():
    print("reload")

def shoot():
    print("shoot")







def play_classique(etat) :
    random_num=random.random()
    if random_num<1.0/3.0 :
        return "dodge"
    else :
        if random_num<2.0/3.0 :
            return "shoot"
        else :
            return "reload"


if __name__ == '__main__':
    main()
