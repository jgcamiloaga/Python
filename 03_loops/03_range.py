###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###
"""
print ("\nrange():")
nums =range(10)# si solo ponemos un numero es de 0 al numero puesto
for num in range(10):
    print(num)

#range (inicio,fin)
for num in range(5,10):
    print(num)

#range(inicio,fin,paso)
for num in range(0,100,5):
    print(num)
for num in range(-5,0):
    print(num)
for num in range (10,0,-1):
    print(num)



nums = range (10)
list_of_nums=list(nums)
print(list_of_nums)

contador = 0
while contador < 5:
    print("hacer cinco veceees algo")
    contador+=1

for _ in range(5):
    print("hacer 5 veces algo ")



for num in range(6):
    print("-")
print(num)



"""

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().

for numero in range (1,11):
    print(numero)



# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

for num in range(1,20,2):
    print(num)



# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
"""
for numero in range(5,51,5):
    print(numero)
"""
for numero in range(5,51):
    if numero %5 == 0:
     print(numero)


# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

for numero in range (11,0,-1):
   print(numero)



# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

acum = 0
for num in range(1,101):
   acum+=num
print(f"La suma es : {acum}")



# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().


usuario= int (input("Introduzca un numeroo: "))
for num in range(1,11):
   print(f" {num} x {usuario} = {num*usuario}")

