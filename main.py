from actor import Actor
from random import randint

p1 = Actor ("Cris", 100, 100, 100)
p2 = Actor ("Sofia", 100, 100, 100)

while p1.is_alive () and p2.is_alive ():
    print (p1, "\n\n", p2, "\n")

    p1.recover ()
    p2.recover ()

    if randint (1, 6) <= 3:
        print (p1.name, "attacks first!")
        p1.attack (p2)
        if p2.is_alive ():
            p2.attack (p1)
    
    else:
        print (p2.name, "attacks first!")
        p2.attack (p1)
        if p1.is_alive ():
            p1.attack (p2)

print (p1, "\n\n", p2, "\n")

if p1.is_alive ():
    print (p1.name, "wins!")
elif p2.is_alive ():
    print (p2.name, "wins!")
else:
    print ("Both", p1.name, "and", p2.name, "died!")