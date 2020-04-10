abecedario = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k",
              12:"l", 13:"m", 14:"n", 15:"ñ", 16:"o", 17:"p", 18:"q", 19:"r", 20:"s", 21:"t",
              22:"u", 23:"v", 24:"w", 25:"x", 26:"y", 26:"z"}

palabra = input("Ingrese una palabra ")
palabram = palabra
letranumero  = " "
palabran = " "

for letra in palabra:

    for llave, valor in abecedario.items():
        if letra.lower() == valor:
            letranumero += str(llave)
            palabran += "" + str(valor) + '('+ str(llave)+')'
print("frase: ", palabram)
print("Salida: ", palabran)