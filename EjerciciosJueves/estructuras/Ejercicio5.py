from collections import Counter

archivo = open('texto.txt', 'r')
texto = archivo.read()
archivo.close()

contp = texto.split()

cont = Counter(contp)

frec= cont.most_common()[0][0]

ocurrencias = texto.count(frec)

print("La palabra que mas se repite es {} con un total de {}".format(frec, ocurrencias))
