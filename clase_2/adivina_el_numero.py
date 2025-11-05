import random

numero = int(random.randrange(1,10))
adivinar = True
while adivinar:
    intento = int(input("Digita un número del 1 al 10: "))
    if intento == numero:
        print("Adivinaste")
        adivinar = False 