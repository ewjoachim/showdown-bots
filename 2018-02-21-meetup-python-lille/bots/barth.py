opact = ""
charger = 1
opcharger = 1
print ("Barth")

print("dodge") #Dodge

while True: 

    if opact == "shoot":
        opcharger -= 1
        if opcharger == 0:
            print("reload")
        else:
            print("shoot")

    if opact == "dodge":
        print("dodge")

    if opact == "reload":
        opcharger += 1
        print("dodge")

    if opact == "stand":
        print("shoot")

    if opact == "shoot_no_bullet":
        print("shoot")

    opact = input() #read the opponent action
