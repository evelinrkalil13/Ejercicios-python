contpar = 0
multpar = 1
contimpar = 0
mulimpar = 1

for i in range (0,101):



    if i == 0:
        contpar = contpar + 1
    elif i % 2 == 0:
        contpar = contpar + 1
        multpar = i * multpar

    elif i % 2 == 1:
        contimpar = contimpar + 1
        mulimpar = i * mulimpar



print("el total de pares es: ", contpar)
print("la multiplicación de los pares es: ", multpar)

print("el total de impares es: ", contimpar)
print("la multiplicación de los impares es: ", mulimpar)