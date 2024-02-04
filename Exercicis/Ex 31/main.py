from calculaIva import calcul
def main():
    valor = float(input("Introdueix un valor en euros  "))
    iva = input("Quin IVA vols 4%, 10% o 21%  ")
    valor,iva, total = calcul(valor,iva)
    print(f"El teu valor es: {valor}")
    print(f"El teu iva es: {iva}%")
    print(f"El total es: {total}")
main()