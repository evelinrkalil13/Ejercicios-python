suma = 0
promedio = 0
n = int(input("Ingrese la cantidad de números a calcular"))
c = 0
contp = 0
contn = 0

while c < n:
  print("Ingrese el número", c)
  m=int(input())

  if m <= 0:
      contn = contn + 1
  elif m > 0:
      contp = contp + 1
  c = c + 1


print ("Los números mayores a 0 son", contp)
print ("Los números menores o iguales a 0 son", contn)
