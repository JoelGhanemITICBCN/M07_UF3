def mostra(num1,num2):
    rango = range(num1, num2 + 1)
    lista = []
    suma = 0
    for num in rango:
        lista.append(num)
        suma += num
    return lista, suma
    