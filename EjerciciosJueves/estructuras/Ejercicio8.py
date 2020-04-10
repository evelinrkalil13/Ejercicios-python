
palabrai = input("Ingrese una palabra ")
palabra = palabrai.lower()

ocurrenciasa = palabra.count("a")
ocurrenciase = palabra.count("e")
ocurrenciasi = palabra.count("i")
ocurrenciaso = palabra.count("o")
ocurrenciasu = palabra.count("u")

print("la palabra tiene: ")
print(ocurrenciasa, "a")
print(ocurrenciase, "e")
print(ocurrenciasi, "i")
print(ocurrenciaso, "o")
print(ocurrenciasu, "u")