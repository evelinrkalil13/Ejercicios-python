promedio = 0
nalum = 0
cont = 1
acom = 0

while nalum < 18:
    print("Ingrese la edad del alumno número ", cont)
    nalum= int(input())

    if nalum != 18:
        acom = acom + nalum
        cont = cont + 1
    else:
        acom = acom
        cont = cont - 1


promedio = acom / cont

print("El promedio es ", promedio )


