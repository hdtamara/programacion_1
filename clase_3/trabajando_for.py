#Generalidades
# lista = [1,"Hola",5,True,"a"]
# for i in lista:
#     print(i)

# print("El ciclo ya culmino")

# i = 0
# for x in range(5):
#     i=i+1
#     print(i)

# lista = []
# for x in range(5):
#      numero = int(input("Digitame un número entero: "))
#      #Elevar al cuadrado
#      numero = numero**2
#      lista.append(numero)
#      print(lista)

# lista = [5,3,5,1,2,3,10,10]
# lista_limpia = []

# for i in lista:
#     if i >= 5:
#         lista_limpia.append(i)
#     print(lista_limpia)


lista = []
for _ in range(5):
    numero = int(input("Digite un número entero: "))
    lista.append(numero)

print("Tu lista es: ",lista)
lista_limpia = []
for i in lista:
    if i%2==0:
        lista_limpia.append(i)
print("Lista de solo pares: ",lista_limpia)