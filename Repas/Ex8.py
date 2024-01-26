num = 0
paraula = input("Digues una paraula    ")
print("Has dit " + paraula)
for letra in paraula:
    num+=1
print("La paraula té " + str(num) + " lletres")
print("La primera lletra és " + paraula[0] + " i la última és " + paraula[-1])