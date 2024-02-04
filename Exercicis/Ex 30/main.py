from salutacio import hola

def main():
    texto = input("Digues un nom que DiGref le manda un saludo: ")
    saludo = hola(texto)
    print(saludo)

if __name__ == "__main__":
    main()