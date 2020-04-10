aux, fib, init = 1, 0, 1

lim = int(input("Ingrese un numero para la sucesion de fibonacci: "))
if lim > 0:
    while init <= lim:
        print(fib, end=" ")
        aux += fib
        fib = aux - fib
        init += 1
    print()
else:
    print("El número debe ser mayor a cero!")