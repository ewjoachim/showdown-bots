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
    etat = etat_game()
    while True :
        etat = play(etat)
        #etat._print()



def update_joueur(joueur,coup) :
    joueur.list_coup_prev.append(coup)
    if coup=="dodge":
        joueur.nb_dodge=joueur.nb_dodge+1
    if coup=="reload":
        joueur.nb_balle=min(6,joueur.nb_balle+1)
    if coup=="shoot" :
        joueur.nb_balle=min(0,joueur.nb_balle-1)
    return joueur

def update_etat(etat,coup_adv,coup) :
    etat.Joueur_adv=update_joueur(etat.Joueur_adv,coup_adv)
    etat.Joueur_moi=update_joueur(etat.Joueur_moi,coup)
    etat.tour=etat.tour+1
    if (coup_adv=="shoot" and coup=="reload" ) or (coup_adv=="dodge" and coup=="reload" ) :
        etat.state="over"
    return etat

def play(etat) :
    coup=strategie_auto(etat)
    if coup=="nothing":
        coup=play_classique(etat)
    print(coup)
    coup_adv=input()
    #print(coup)
    etat=update_etat(etat,coup_adv,coup)
    return etat

def strategie_auto(etat) :
    moi = etat.Joueur_moi
    adv = etat.Joueur_adv
    if (100-etat.tour<moi.nb_balle) and (moi.nb_dodge+moi.nb_balle<=adv.nb_dodge+moi.nb_balle) :
        return "shoot"
    if (moi.nb_dodge+100-etat.tour<adv.nb_dodge) :
        return "dodge"
    return "nothing"


def play_classique(etat) :
    cst_shoot=2.0
    cst_reload=1.0
    cst_dodge=4.0
    proba_dodge = 1.0
    proba_shoot = 1.0
    proba_reload = 1.0
    nb_ball_adv = etat.Joueur_adv.nb_balle
    nb_ball_moi = etat.Joueur_moi.nb_balle
    nb_dodge_adv = etat.Joueur_adv.nb_dodge
    nb_dodge_moi = etat.Joueur_adv.nb_dodge

    proba_shoot = max(0,proba_shoot * (1 + 1.0*cst_shoot * (nb_ball_moi - nb_ball_adv) / 6))
    proba_dodge = max(0,proba_dodge * (1 + 1.0*cst_dodge * (nb_ball_adv - nb_ball_moi) / 6))
    proba_reload = max(0,proba_reload * (1 + 1.0*cst_reload * (nb_dodge_adv - nb_dodge_moi) / 6))

    if nb_ball_moi==0 :
        proba_shoot=0
    if nb_ball_adv == 0:
        proba_dodge=0
    if nb_ball_moi==6 :
        proba_reload==0
    if nb_ball_adv==6 :
        proba_shoot==0

    random_num = random.uniform(0, proba_shoot + proba_reload + proba_dodge)

    #print(nb_ball_adv)
    #print(nb_ball_moi)
    #print(proba_dodge)
    #print(proba_shoot)
    #print(proba_reload)
    #print(random_num)

    if random_num<proba_dodge :
        return "dodge"
    else :
        if random_num<proba_dodge+proba_shoot :
            return "shoot"
        else :
            return "reload"


if __name__ == '__main__':
    main()