lista_1 = ["C", "C++", "Python", "Java"]
print(lista_1[0])
#Append inserta un nuevo elemento a la lista, al final
lista_1.append("Go")
print(lista_1)
#Remover un elemtno de la lista
lista_1.pop(0)
print(lista_1)
print(lista_1[0])
#Reemplazar elementos de la lista
lista_1[1]="R"
print(lista_1)
# Contar cuantos elementos tiene la lista
print(len(lista_1))
#Acceder al ultimo elemento de la lista.
#Metodo 1
ultimo_index = len(lista_1)-1
print(lista_1[ultimo_index])
#Metodo 2
print(lista_1[-1])
lista_1.reverse()
print(lista_1)

