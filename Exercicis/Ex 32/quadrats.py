def calcul(valors):
    valorsSeparats = (valors.split())
    valorsSeparatsInt = []
    valorsQuadrats = []
    for num in valorsSeparats:
        valorInt = int(num)
        valorsSeparatsInt.append(valorInt)
    for valor in valorsSeparatsInt:
        valorQuadrat = valor * valor
        valorsQuadrats.append(valorQuadrat)
    return valorsQuadrats