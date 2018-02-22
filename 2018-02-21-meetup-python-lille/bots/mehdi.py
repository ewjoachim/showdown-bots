from random import *
a=0
def count(p):
    k=0
    if p==action[0] or p==0:
        k=1
    elif p==action[1] or p==1:
        k=-1
    return k
print("Mehdi")
action=["reload","shoot","dodge"]
countme=1
countother=1
print(action[2])
countme+=count(2)
other=input()
countother+=count(other)

if other==action[1]:
    print("dodge")
    countme+=count("dodge")
    other=input()
    countother+=count(other)
    print("dodge")
    countme+=count("dodge")
    other=input()
    countother+=count(other)
    while True:
        while countme<2:
            a=randint(0,2)
            print(action[a])
            countme+=count(a)
            other= input()
            countother+=count(other)
        for i in range (countme):
            print(action[1])
            countme+=count(1)
            other=input()
            countother+=count(other)
elif other==action[0]:
    print("dodge")
    countme+=count(2)
    other=input()
    countother+=count(other)
    print("dodge")
    countme+=count(2)
    other=input()
    countother+=count(other)
    while True:
        while countme<5:
            a=randint(0,2)
            print(action[a])
            countme+=count(a)
            other= input()
            countother+=count(other)
        for i in range (countme):
            print(action[1])
            countme+=count(1)
            other=input()
            countother+=count(other)

elif other==action[2]:
    print("shoot")
    countme-=1
    other=input()
    countother=count(other)
    while True:
        if countme<2:
            if countme>=1:
                a=randint(0,1)
                print(action[a])
                countme+=count(a)
                other=input()
                countother+=count(other)
            else:
                print (action[0])
                countme+=count(0)
                other=input()
                countother+=count(other)
        else:
            for i in range (countme):
                print (action[1])
                countme+=count(1)
                other=input()
                countother+=count(other)
    
    
