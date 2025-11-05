frase = input("Dame una frase: ")
letra_1 = input("Digita una letra: ")
letra_2 = input("Digita otra letra: ")
# contar cuantas veces aparece la letra 1
print(f"La {letra_1} aparece: {frase.count(letra_1)} veces")
# contar cuantas veces aparece la letra 2
print(f"La {letra_2} aparece: {frase.count(letra_2)} veces")
frase_modificada = frase.replace(letra_1,letra_2)
print(frase_modificada)
print(frase_modificada.upper())