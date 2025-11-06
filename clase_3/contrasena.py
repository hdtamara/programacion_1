import time
secret = "daniela123"
intentos = 3
contador = 0

for _ in range(intentos):
    # contador = contador + 1
    contador +=1
    password = input("Ingrese su contraseña: ")
    if password == secret:
        print("Login exitoso, te has logueado correcto")
        break
    else:
        print("Login fallido intente nuevamente")
    print("números de intentos: ",contador)
    if contador >= 3:
        print("Ha excedido el número de intentos, cuenta bloqueada")
        print('Autodestrucción en: ')
        conteo=3
        for i in range(3):
 
            time.sleep(2)
            print(conteo)

            if conteo == 1:
                print("¡¡BOOM 🧨🧨🧨!!")
            conteo-=1