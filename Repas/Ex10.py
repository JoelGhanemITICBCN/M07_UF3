import random
num = random.randint(1,100)
numMesGran = 0
##print(num)
print("Has d'endevinar un número entre l'1 i el 100")
numJugador = int(input("Digues un número   "))
numMesPetit = numJugador
while (num != numJugador):
    if (num > numJugador):
        if(numMesGran <= numJugador):
            numMesGran = numJugador
        numJugador = int(input("Digues un del " + str(numMesGran) + " al 100   "))
    else:
        """
        print("Num mes petit")
        print(numMesPetit)
        print("numJugador")
        print(numJugador)
        """
        if(numMesPetit >= numJugador):
            numMesPetit = numJugador
        numJugador = int(input("Digues un del " + str(numMesPetit) + " al 0   "))
print("Correcte! el numero era " + str(num))