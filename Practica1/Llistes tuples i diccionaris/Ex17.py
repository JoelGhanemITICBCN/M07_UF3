## Variable global

letrasGuardadas =""
arrayGuardador = []
frase = input("Digues una frase i et mostrare pr tuple els caracters sense repetir:       ")
fraseSeparada = (frase.split())
for palabra in fraseSeparada:
    for letra in palabra:
        if letra not in letrasGuardadas:
            letrasGuardadas += letra
    arrayGuardador.append(letrasGuardadas)
    letrasGuardadas = ""    
aLaTupla = arrayGuardador
tupla = tuple(aLaTupla)
print(aLaTupla)