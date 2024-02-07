lletresDites = ""

paraules = input("Digues 2 paraules i dire quantes vegades apareix cada lletra: ")
tupla = tuple(paraules.split())
print(tupla)

for paraula in tupla:
    for lletra in paraula:
        if lletra not in lletresDites:
            lletresDites += lletra
            comptador = paraules.count(lletra)
            print(f"La lletra {lletra} apareix {comptador} cops")
