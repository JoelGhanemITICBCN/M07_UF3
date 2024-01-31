numeros = input("Digues 10 numeros separats per un espai:      ")
numerosSeparats = (numeros.split())
numerosSeparats = [int(num) for num in numerosSeparats]
numerosSeparats.sort()
tupla = tuple(numerosSeparats)
print(str(tupla))