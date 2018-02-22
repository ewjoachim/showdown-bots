import random

name = "Morgan"

print(name)

random_num = random.random()

while True :

    if random_num < 1.0 / 2.0 :
        print("dodge")
    else :
        if random_num < 2.0 / 3.0 :
            print("shoot")
        else :
            print("reload")
    balec = input()
