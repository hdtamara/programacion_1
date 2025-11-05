numero_1 = float(input("Digita el primer número: "))
numero_2 = float(input("Digita el segundo número: "))
if numero_1 > numero_2:
    print(f"{numero_1} es mayor que {numero_2}")
elif numero_1 == numero_2:
    print("Ambos números son iguales")
else:
    print(f"{numero_1} es menor que {numero_2}")