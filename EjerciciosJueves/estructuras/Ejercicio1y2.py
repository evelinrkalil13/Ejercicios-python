
calificaciones = {'calculo':10 , 'dibujo':5}
valores = calificaciones.values()
promedio = 0
cont = 0;
itemant = 0




print("Sus notas son:")

for valor in valores:
    cont = cont + 1
    promedio = promedio + valor
    print(valor)

promedio = promedio/cont
print("y su promedio es de: ", promedio)

notac =calificaciones.get("calculo")
notad =calificaciones.get("dibujo")

if notac > notad:
    print("Su mejor calificación es calculo")

else:
    print("Su mejor calificación es dibujo")