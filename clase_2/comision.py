nombre = input("Digita tu nombre: ")
ventas = float(input("Ingresa tus ventas de este mes: "))
comision = ventas * 0.13
comision = round(comision,2)
print(f"Hola {nombre} tu comisión para este mes es {comision}")
