paraula1 = input("Digues una paraula     ")
paraula2 = input("Digues una més         ")
paraula1Nova = paraula2[:2] + paraula1[2:]
paraula2Nova = paraula1[:2] + paraula2[2:]
print("La primera paraula canviada: " + paraula1Nova + " La segona paraula canviada: " + paraula2Nova)