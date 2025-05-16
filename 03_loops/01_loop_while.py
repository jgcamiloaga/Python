###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###
"""
print("\n Bucle while: ")
#Bucle con una simple condicion
contador=0
while contador <= 5:
    print(contador)
    contador +=1 #Es super importante para evitar un bucle infinito
#Utilizando la palabra break, para romper el bucle
print("\n Bucle while con break: ")
contador = 0
while True:
    print(contador)
    contador +=1
    if contador ==5:
        break #sale del bucle

#Continue, que lo hace es saltar esa 
#iteracion en concreto y continuar con el bucle
print("\n Bucle con continue")
contador=0
while contador<10:
    contador +=1
    if contador %2 ==0:
        continue
    #👇
    print(contador)

#else esta condicion cuando se ejecuta?
print("\n Bucle con else")
contador=0
while contador<5:
    print(contador)
    contador +=1
    break
else:
    print("El bucle a terminado")


#pedirle al usuario un numero que tiene
#que ser positivo si no,no le dejamos en paz
numero=-1
while numero <0:
    numero=int(input("Escribe un numero positivo: *"))
    if numero < 0:
        print("El numero debe ser positivo.Intentaotra vez")
print(f"El numero que haz introducido es {numero}")



numero=-1
while numero <0:
    try:
        numero=int(input("Escribe un numero positivo: *"))
        if numero < 0:
            print("El numero debe ser positivo.Intenta otra vez")
    except:
        print("Lo que introduces debe ser un numero, que si o no peto!")
print(f"El numero que haz introducido es {numero}")

"""









###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

"""
contador = 10
while contador > 0:
     
     print(contador)
     contador-=1
 """  

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
"""
contador =0
acumulador = 0
while contador<20:
    contador+=1
    if contador %2 ==0:
        acumulador+=contador
print("La suma es: ",acumulador)
"""
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.


num_pos= int(input("Ingrese un numero que sea entero positivo: "))
factorial=1
contador =1
while contador<= num_pos:
    factorial *=contador
    contador +=1
print(f"El factorial de {num_pos} es: ",factorial)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

contraseña= ""
while len(contraseña)<8:
    contraseña =input("Ingrese su contraseña: ")
    if len(contraseña)<8:
        print("La contraseña debe tener al menos 8 caracteres")
print("Contraseña valida")




# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.





# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.




