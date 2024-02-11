
numeros = input("Digues  numeros separats per un espai que jo tallare en el 0:      ")
numerosSeparats = (numeros.split())
numerosSeparatsInt = []
for num in numerosSeparats:
    numInt = int(num)
    if numInt == 0: 
        break
    numerosSeparatsInt.append(numInt)
numerosSeparatsInt.sort()
tupla = tuple(numerosSeparatsInt)
print(str(tupla))