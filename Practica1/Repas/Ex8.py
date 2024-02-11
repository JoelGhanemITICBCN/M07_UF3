num = 0
paraula = input("Digues entre una i tres paraules    ")
print("Has dit " + paraula)
paraula2 = ""
paraula3 = ""
paraules = paraula.split()
if len(paraules) >= 1:
    paraula = paraules[0]
if len(paraules) >= 2:
    paraula2 = paraules[1]
if len(paraules) >= 3:
    paraula3 = paraules[2]
for letra in paraula:
    num += 1
print("La paraula " + paraula + " té " + str(num) + " lletres")
print("La primera lletra és " + paraula[0] + " i la última és " + paraula[-1])
if paraula2 != "":
    num = 0
    for letra in paraula2:
        num += 1
    print("La paraula " + paraula2 + " té " + str(num) + " lletres")
    print("La primera lletra és " + paraula2[0] + " i la última és " + paraula2[-1])
if paraula3 != "":
    num = 0
    for letra in paraula3:
        num += 1
    print("La paraula " + paraula3 + " té " + str(num) + " lletres")
    print("La primera lletra és " + paraula3[0] + " i la última és " + paraula3[-1])