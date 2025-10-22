lado_1 = float(input("Digite el lado 1: "))
lado_2 = float(input("Digite el lado 2: "))
lado_3 = float(input("Digite el lado 3: "))

if lado_1+lado_2>lado_3 and lado_2+lado_3>lado_1 and lado_3+lado_1>lado_2:
    print("Es un triangulo")
    #validamos si es equilatero
    if lado_1==lado_2==lado_3:
        print("Es un trinagulo equilatero")
    #validamos si es isoceles
    elif lado_1==lado_2 or lado_2==lado_3 or lado_3==lado_1:
        print("Es un tringulo isoceles")
    else:
        print("Es escaleno")
else:
    print("No es un trinagulo")