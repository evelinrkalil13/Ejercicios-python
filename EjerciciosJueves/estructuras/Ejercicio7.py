
palabra = input("Ingrese una palabra ")

def obtener_vocales(frase):
    vocales = 'aeiouAEIOU'

    return [c for c in frase if c in vocales]


print("la palabra" ,'"',palabra,'"', "tiene ",len(obtener_vocales(palabra)), " vocales")
print("Que son: ")
print(obtener_vocales(palabra))