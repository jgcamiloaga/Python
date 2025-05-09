###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

print("\n crear listas")
lista1 = [1,2,3,4,5] #Lista de enteros
lista2 = ["manzana","peras","platanos"]#lista de cadenas
lista3: list [int| str |float |bool] = [1,"hola", 3.24,True] #lista de tipos mixtos
lista_vacia =[]
lista_de_listas =[(1,2) , [(3,4)]]
matrix =[(1,2)],[(2,3)],[("calcetin",5)]


print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)


#Acceso a elementos por indice
print("\nAcceso a elementos por inidice")
print(lista2[0])
print(lista2[1])
print(lista2[-1])
print(lista2[-2])
#0-1-2....
#-3,-2-1

print(lista_de_listas [1][0])

#slicing (rebanado) de listas
lista1 = [1,2,3,4,5]

print(lista1 [1:4]) #[2,3,4]
print(lista1[:3]) # [1,2,3]
print(lista1[3:]) #[4,5]
print(lista1[:]) #[1,2,,4,5]

#Hay mas magia
lista1 = [1,2,3,4,5,6,7,8]
print(lista1[::2])#[1.4.7] para devolver indices pares
print(lista1[::-1])#[8-7-6-5-4-3-2-1] para devolver indices impares
#print(lista1[desde:hasta:paso])

#MODIFICAR UNA LISTA
lista1[0] = 20
print(lista1)
#forma mas larga y menos eficiente
lista1 =lista1 + [4,5,6]
print(lista1)

#forma mas corta
lista1 += [7,8,9]


#recuperar longitud de una lista
print("Longitud de la lista", len(lista1))

###
# EJERCICOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
lista = mensaje[7:]
print(lista)



# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
print(numeros)
numeros [0] = 50
numeros [-1] = 10
print(numeros)




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




