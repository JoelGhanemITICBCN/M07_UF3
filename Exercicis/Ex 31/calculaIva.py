def calcul(valor,iva):
    iva = float(iva)
    total = valor + (valor * iva/100)
    return valor,iva,total
