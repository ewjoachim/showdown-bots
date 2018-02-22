##Imports
from random import random as rand



## Fonctions
def compteurAmmo(other, ammoA):
    if other == "shoot":
        ammoA -= 1
    elif other == "reload":
        ammoA += 1
    return ammoA
    
def action(shootR, reloadR, dodgeR):
    pt = rand()*100
    if shootR[0] <= pt and pt <= shootR[1]:
        action = "shoot"
    elif reloadR[0] <= pt and pt <= reloadR[1]:
        action = "reload"
    else:
        action = "dodge"
    return action
        
    
def ajusteS(shootR, reloadR, dodgeR):
    reloadR[0] = shootR[1]
    if shootR[1] > reloadR[1]:
        reloadR[1], dodgeR[0] = shootR[1], shootR[1]
    return shootR, reloadR, dodgeR
    
def ajusteR(shootR, reloadR, dodgeR):
    shootR[1],dodgeR[0] = reloadR[0], reloadR[1]
    return shootR, reloadR, dodgeR
    
def ajusteD(shootR, reloadR, dodgeR):
    reloadR[1] = dodgeR[0]
    if dodgeR[0] < reloadR[0]:
        reloadR[0], shootR[1] = dodgeR[0], dodgeR[0]
    return shootR, reloadR, dodgeR



##Principal

print("Ben")
count = 1
ammo = 1
ammoA = 1
compteR = 0
compteS = 0
compteD = 0

shootR = [0,10]
reloadR = [10,20]
dodgeR = [20, 100]
other = ""

a = ["shoot","dodge","reload","stand","shoot_no_bullet"]
(sh, do, re, st, sn) = (0,1,2,3,4)
while True:
    
    
    if ammo >= 2:
        reloadR = [50,50]
        shootR, reloadR, dodgeR = ajusteR(shootR, reloadR, dodgeR);
    
    if other == "reload":
        shootR = [0, 20]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
        compteR += 1
        compteS = 0
        compteD = 0
        ammoA += 1
    
    if other == "shoot":
        shootR = [0, 30]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
        reloadR = [30, 85]
        shootR, reloadR, dodgeR = ajusteR(shootR, reloadR, dodgeR);
        compteS += 1
        compteD = 0
        compteR = 0
        ammoA -= 1
        
    if other == "dodge":
        compteD += 1
        compteS = 0
        compteR = 0    
    
    if compteD != 0:
        sho = shootR[1]-shootR[0]
        sho = sho * compteD 
    
        shootR = [0,sho]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
        
        
    
    
    if ammoA == 0:
        shootR = [0,40]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
        dodgeR = [100,100]
        shootR, reloadR, dodgeR = ajusteD(shootR, reloadR, dodgeR);
        
    if ammo == 0:
        reloadR = [0,75]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
        
    if other == "stand" or other == "shoot_no_bullet":
        shootR = [0,100]
        shootR, reloadR, dodgeR = ajusteS(shootR, reloadR, dodgeR);
         
    
        
        
        
        
        
        
    act = action(shootR, reloadR, dodgeR);
    
    if act == "shoot":
        ammo -= 1
    elif act == "reload":
        ammo += 1
    
    print(act)
        

    
    other = input()
    
    
    