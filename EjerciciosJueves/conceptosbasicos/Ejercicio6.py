print("Numero de vueltas que da una llanta de 50 cm en un kilometro:")

#se ontiene la longitud de la llanta es decir, cuanto recorre en cada vuelta

circunferencia = 3.1416 * 50

# Ahora debemos homologar las medidas 1km= 100000 cm

circunferencia = circunferencia/100000

#Y por ultimo obtenemos la cantidad de vueltas de la llanta en un km

longitud = 1/circunferencia

print(longitud)