numeros = input("Digues 10 numeros separats per espais:  ")
llista = (numeros.split())
suma = 0
for num in llista:
    suma += int(num)
mitjana = suma/len(llista)
print(f"Números de l’usuari: {llista}")
print(f"Suma total: {suma}")
print(f"Mitjana: {mitjana}")