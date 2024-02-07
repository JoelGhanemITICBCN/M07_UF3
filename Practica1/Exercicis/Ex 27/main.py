from calculadora import suma

def main() :
    num1 = int(input("Digues un num:  "))
    num2 = int(input("Digues un num:  "))
    resultat = suma(num1,num2)
    print(f"La suma es: {resultat}")
main()
