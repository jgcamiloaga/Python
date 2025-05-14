###
# 04 - Listas métodos
# Los métodos más importantes
###
import os
os.system("clear")
lista1 =[1,2,3,4,5]
#AÑADIR O INSERTAR ELEMENTOS A LA LISTA

lista1.append('e') #añade un elemento al final
print(lista1)
lista1.insert(1,'@') #Inserta un elemento en la posicion
#que le  indiquemos como primer argumento
print(lista1)

lista1.extend(['📚','💻'])#Agrega elementos al final de
#la lista
print(lista1)


#ELIMINAR ELEMENTOS DE LA LISTA
lista1.remove('@')#Elimina la primera paricion de la cadena de texto @
print(lista1)
ultimo=lista1.pop()#eliminar el ultimo elemento de la lista 
#y ademas te lo devuelve  (1)--posicion 1 eliminada
print(ultimo)
print(lista1)
lista1.pop(1)#Eliminar el segundo elemento de la lista (es el indice 1)
#Eliminar por lo bestia--rangossssssssssss
print(lista1)
del lista1[-1]
print(lista1)

lista1.clear()#Eliminar todos los elementos de la lista
print(lista1)

#Eliminar un rango de elementos
lista1 =['🐼','🦝','🐮','🐻‍❄️']
del lista1[1:3]
print(lista1)

#Mas metodos utiles
print('Ordenar listas modificando la original  ')
numbers = [3,10,2,8,99,101]
numbers.sort()#ordena la lista de menor a mayor
print(numbers)

print('Ordenar listas creando una lista ')
numbers=[3,10,2,8,99,101]
sorted_numbers =sorted(numbers)
print(sorted_numbers)


print('Ordenar una lista de cadenas de texto '
'(todo minuscula)')

#hasta la mitad---no modifica-------importa la mayucula>
frutas =['manzana','pera','limon','manzana','pera','limon']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

#Alinamiento directo
print("Ordenar una lista de cadenas de texto(mezclas mayus y minus)")
frutas =['manzana','pera','limon','Manzana','pera','limon']
frutas.sort(key=str.lower)#upper
print(frutas)

#Mas metodos utiles
animals =['🐼','🐻','🐮','🐼']
print(len(animals))#Tamaño de las listas ->4
print(animals.count('🐼'))#cuantas veces aparece 
#el elemento->2

print('🐮' in animals)# comprueba si hay una vaca  en la lista->true
print('🐸' in animals)#false











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




