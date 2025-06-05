###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###
"""
print("\n Bucle for: ")
#Iterar una lista
frutas  = ["manzana","pera","mandarina"]
for fruta in frutas:
    print(fruta)

#Iterar sobre cualquier cosa que sea iterable
cadena ="dana"
for caracter in cadena :
    print(caracter)

#enumerate()
frutas =["manzana","pera","mandarina"]
for idx,value in enumerate(frutas):
    print(f"El indice es {idx} y la fruta es {value}")


#bucles anidados -meter uno dentro de otro for dentro de otro y asi 
letras=["a","b","c"]
numeros =[1,2,3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

#break
animales =["perro","gato","raton","loro","pez","canario"]
for idx,animal in enumerate(animales):

    if animal =="loro":
      continue
    print(animal)

"""
animales =["perro","gato","raton","loro","pez","canario"]
animales_mayus=[animal.upper() for animal in animales]
print(animales_mayus)

#muestra los numeros pares de una lista 
pares = [num for  num in [1,2,3,4,5,6] if num % 2 ==0]
print (pares)

"""
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
"""
for num in range (2,21):
    if num % 2 == 0:
        print(num)

for num in range (2,21,2):
    print (num)
"""

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
"""
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
cont= 0
acum=0
for num in numeros:
    acum+= numeros [cont]
    cont+=1
promedio = int (acum/cont)
print (f"La media de los numeros es : {promedio}")


"""
# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
"""
print("\nEjercicio 3:")

numeros = [15, 5, 25, 50, 20]
maximo = numeros[0]
for num in numeros:
    if num >maximo:
        maximo =num
print(f"El numero maximo es : {maximo}")
    

"""

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
"""

palabras = ["casa", "arbol", "sol", "elefante", "luna","california"]
mas_de_5 =[]
for letra in palabras:
    if len(letra)>5:
        mas_de_5.append(letra)
print(f"Las palabras que tienen mas de 5 letras son : {mas_de_5}")

print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna","california"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)

"""

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
contador = 0

while (contador==0):
    respuesta = input("Ingrese una letra: ").upper()

    for palabra in palabras:
        if palabra.upper().startswith(respuesta):
            contador+=1

print (f"Existen la cantidad de : {contador}")


"""