from quadrats import calcul
def main():
    valors = input("Digues 10 digits separats per un espai:  ")
    valorsQuadrats = calcul(valors)
    print(f"{valorsQuadrats}")
main()