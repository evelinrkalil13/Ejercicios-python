lista=[]
palabra = " "
while palabra!="0":
    lista.append(palabra)
    palabra = str(input("Ingresar valor (0 para finalizar):"))
    if str(palabra) == "0":
        print("Fin del programa")
    elif str(palabra) == str(palabra)[::-1]:
        print("Es palindroma")
    else:
        print("No es palindroma")

