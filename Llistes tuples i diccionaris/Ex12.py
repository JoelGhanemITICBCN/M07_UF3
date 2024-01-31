tupla = tuple(["Gener","Febrer","Març","Abril","Maig","Juny","Juliol","Agost","Setembre","Octubre","Novembre","Decembre"])
numUsuari = int(input("Digues un número entre l'1 i el 12       "))
while(numUsuari != 0)    :
    print(tupla[numUsuari-1])
    numUsuari = int(input("Digues un altre número entre l'1 i el 12       "))
print ("adeu")