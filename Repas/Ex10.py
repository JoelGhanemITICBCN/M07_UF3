import random
num = random.randint(1,100)
##print(num)
print("Has d'endevinar un número entre l'1 i el 100")
numJugador = int(input("Digues un número   "))
while (num != numJugador):
    if (num > numJugador):
        numJugador = int(input("Digues un més gran   "))
    else:
        numJugador = int(input("Digues un més baix   "))
print("Correcte! el numero era " + str(num))