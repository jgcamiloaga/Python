###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

import os
os.system("clear")

# Crear una lista
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["a", "b", "c", "d", "e"] # Lista de strings
lista3 = [1, "a", 3.14, True] # Lista mixta

# Lista vacía 
lista4 = []
lista_de_listas = [[1, 2, 3], ["Pera", 5, 6], [7, 8, 9]]
matrix = [[1,2], ["Manzana",4], [5,6]]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)
print("Lista 4:", lista4)
print("Lista de listas:", lista_de_listas)
print("Matrix:", matrix)

#Acceder a elementos de una lista
print("\nAcceder a elementos de una lista")
print("Primer elemento de la Lista 1: ", lista1[0])
print("Lista de lista: ", lista_de_listas[1][0])

# Slicing (rebanado)
listaNueva = [1,2,3,4,5,6,7,8,9,10]
print(listaNueva[:2+1])
print(listaNueva[-3:])
print(listaNueva[:]) # Copia de la lista

# Más sobre las listas
#print(listaNueva[desde:hasta:paso]) - Slicing con paso
print(listaNueva[1::2]) # Elementos pares
print(listaNueva[::2]) # Elementos impares
print(listaNueva[::-1]) # Invertir una lista

# Modificar elementos de una lista
listaNueva[0] = 100
print(listaNueva)

# Añadir elementos a una lista
listaNueva_2 = [1,2,3]
print(listaNueva_2)

# Forma larga y menos eficiente
listaNueva_2 = listaNueva_2 + [4,5,6]
print(listaNueva_2)

# Forma corta y más eficiente
listaNueva_2 += [7,8,9]
print(listaNueva_2)

# Recuperar logitud de una lista
print("Longitud de la lista:", len(listaNueva_2))

###
# EJERCICOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]