agenda = {}

while True:
    nom = input("Introdueix el nom del contacte (o 'stop' per acabar): ")
    
    if nom.lower() == 'stop':
        break 


    if nom in agenda:
        print(f"Ja hi ha un contacte amb el nom {nom}. No s'afegirà al diccionari.")
    else:
        edat = input(f"Introdueix l'edat de {nom}: ")
        agenda[nom] = int(edat)

print("Diccionari d'agenda:")
for nom, edat in agenda.items():
    print(f"{nom}: {edat} anys")
