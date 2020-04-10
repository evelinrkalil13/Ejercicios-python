
promedio = 0
nalum = 0
cont = 1
acom = 0
correcto = True

while correcto == True:

    try:
        nalum = float(input("Introduce la estatura: "))
        correcto = True
        acom = acom + nalum
        cont = cont + 1
    except ValueError:
        print('se ha introducido una estatura inválida, fin del programa')
        correcto = False
        acom = acom
        cont = cont - 1

promedio = acom / cont

print("El promedio es ", promedio )
