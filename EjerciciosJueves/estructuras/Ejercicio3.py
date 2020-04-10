lista=[]
suma = 0
cont = 0
valor = 0
while cont<10:
    valor = int(input("Ingrese un número"))
    lista.append(valor)
    cont = cont + 1
    suma = suma + valor

promedio = suma/10
print("La suma es igual a ", suma)
print("El promedio es de ", promedio)

print("El número mayor es: ", max(lista))
print("El número menor es: ", min(lista))