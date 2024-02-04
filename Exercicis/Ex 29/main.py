from mostraEnters import mostra
def main():
    num1 = int(input("Digues un num:  "))
    num2 = int(input("Digues un num:  "))
    lista, suma = mostra(num1,num2)
    print(f"Els numeros entre {num1} i {num2} son {lista}")
    print(f"La suma dels valors es: {suma}")
main()
