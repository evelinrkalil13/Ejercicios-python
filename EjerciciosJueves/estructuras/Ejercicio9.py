
texto = input("Ingrese una palabra ")

def eliminar_vocales(palabra):
	vocales = ['a','A','e','E','i','I','o','O','u','U']
	result = ''

	for letra in palabra:
		if letra not in vocales:
			result += letra
	return result

print (eliminar_vocales(texto))