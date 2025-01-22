# Condiciones en Python

import os
os.system("clear")

edad = 15
carnet = True

if edad >= 18 and carnet:
    print("Puede votar")
elif edad >= 18 and not carnet:
    print("No puede votar")
else:
    print("No puede votar")


# Asignación de variables
# En Python, las variables se asignan con el operador =.
ejemplo = 15

# Comparación de variables
# En Python, las variables se comparan con el operador ==.
print(ejemplo == 15) # True


print("\nLa condición ternaria:")
# es una forma de escribir una condición if en una sola línea.
# Sintaxis: valor_si_cierto if condición else valor_si_falso

edad = 20
mensaje_1 = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

print(mensaje_1)

carnet = False
mensaje_2 = "Puedes votar porque tienes carnet" if carnet else "No puedes votar porque no tienes carnet"

print(mensaje_2)

###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)