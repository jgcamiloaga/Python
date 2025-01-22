###
# 04 - Listas métodos
# Los métodos más importantes
###

import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd', 'e']

lista1.append('f') # Añade un elemento al final de la lista
print("append():", lista1)

lista1.insert(0, 'z') # Inserta un elemento en la posición indicada
print("insert():", lista1)

lista1.extend(['g', 'h', 'i']) # Añade varios elementos al final de la lista	
print("extend():", lista1)

lista1.remove('z') # Elimina el primer elemento con el valor indicado - La primera aparición
# No se para el indice sino el valor
print("remove():", lista1)

ultimo = lista1.pop() # Elimina el elemento en la posición indicada
print("Ultimo: " + ultimo)
print("pop():", lista1)

del lista1[-1] # Elimina el elemento en la posición indicada
print("del:", lista1)

lista1.clear() # Elimina todos los elementos de la lista

#Eliminar un rango de elementos
lista1 = ['a', 'b', 'c', 'd', 'e']
print("Lista original:", lista1)
del lista1[-3:]
print("del con rango:", lista1)

# Más metodos
lista2 = [55,99,612,1,3,47,85]
print("Lista 2 sin ordenar:", lista2)
lista2.sort() # Ordena la lista
print("sort():", lista2)

#Ordenar una lista creando una nueva lista
lista2 = [55,99,612,1,3,47,85]
print("Lista 2 sin ordenar:", lista2)
lista2_ordenada = sorted(lista2)
print("sorted():", lista2_ordenada)

#Ordenar una lista de cadenas(Todo minuscula)
frutas = ['manzana', 'Pera', 'naranja', 'kiwi']
print("Frutas sin ordenar:", frutas)
lista2_ordenar = sorted(frutas)
print("Frutas ordenadas:", lista2_ordenar)

#Ordenar una lista de cadenas(mezcalndo mayusculas y minusculas)
frutas = ['manzana', 'Pera', 'naranja', 'kiwi', 'Banana', 'Fresa', 'mango']
print("Frutas sin ordenar:", frutas)
frutas.sort(key=str.lower)
print("Frutas ordenadas:", frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.