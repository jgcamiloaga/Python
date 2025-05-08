###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = input (" Escribe tu nombre: ")
ciudad = input(" Nombre de tu ciudad: ")

print(f"Tu nombre es {nombre}  \n Vives en la ciudad de {ciudad}")




print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
entero = int (cadena)
decimal = float(entero)
print(cadena)
print(entero)
print(decimal)
x = 3.99 
print(int(x))
print(round(x))

# SE IMPRIME EL NUMERO 3, ES DECIR, SE REDONDEA PARA ABAJO

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nom = input("Tu nombre: ")
edad = int (input("Escribe tu edad: "))
altura = float( input("Ingrese su altura: "))

print(f"Hola! Me llamo {nom} y tengo {edad}, mido {altura} metros")



print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí

import math as m

PI = m.pi

PI_redondeado = round(PI)

division_entera = PI_redondeado // 2
print(division_entera)
 # / normal
 # // el entero del decimal





