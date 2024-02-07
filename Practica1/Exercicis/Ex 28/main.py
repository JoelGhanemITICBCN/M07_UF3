from randomNum import numAleatori 

def main():
    num1 = int(input("Digues un num:  "))
    num2 = int(input("Digues un num:  "))
    resultat = numAleatori(num1,num2)
    print(f"Un num aleatori entre el {num1} i el {num2} es el {resultat}")
main()