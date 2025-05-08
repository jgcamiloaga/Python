# Condiciones en Python
print("\n Sentencia simple condicional")

edad = 18

if edad>= 18 :
    print("Eres mayor de edad")
    print("Felicidades")
print("\n Sentencia condicional con else")
edad =15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("\n Sentencia condicional elif")
nota = 7
if nota >= 9:
    print("sobresaliente")

elif nota >=7:
    print("Notable")
elif nota>= 5:
    print("aprobado")
else:
    print("No estas calificado")


print("\n condiciones multiples")
edad = 25
tiene_carnet = True
#javascript
#&& -> and
#|| -> or
if edad >=18 and tiene_carnet:
    print("puedes conducir")
else:
    print("Policia!!!!!!!!!!!!")

if edad >=18 or tiene_carnet:
    print("puedes conducir")
else:
    print("paga al policia y te deja conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Hay que estudiar")


print("\n Anidar condiciones")
edad =20
tiene_dinero = True
if edad>=18:
 if tiene_carnet:
    print("Puedes ir a la fiesta")
 else:
    print("Quedate en casa")
else:
   print("Nopuedes ir a la fiesta")
# Mas facil
if edad < 18:
   print("No puedes entrar")
elif tiene_carnet:
 print("puedes ir a la fiesta")
else:
   print("Quedate en casa")



numero = 5
if numero: #true
   print("El numero no es 0")

numero= 0
if numero: #false
   print(("Aqui no entrara nunca"))

nombre = ""
if nombre:
   print("El nombre no esta vacio")
   numero =3#asignacion
   es_el_tres = numero =3 #comparacion
   if es_el_tres:
    print("El numero es 3")


print ("\nLa condicion ternaria")

edad=17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
"""
num1 = int(input("Escriba un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 > num2:
   print(f"El primer numero {num1} es mayor")
elif num2 >num1:
   print(f"El segundo numero {num2} es mayor")
else:
   print("Son iguales")
"""


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
"""
numero1 = int (input("Ingrese un valor: "))
numero2 = int (input("Ingrese el segundo valor: "))
operacion = input("Operacion que quieras realizar: ")

if operacion == "+" :
   resultado = numero1 + numero2
elif operacion == "-":
   resultado = numero1 - numero2
elif operacion == "*":
   resultado = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
      resultado =numero1 / numero2
    else:
      resultado = "ERROR"
else:
   resultado = "No se encuentra operacion"

print(resultado)
"""


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
"""
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año %100 != 0) or (año % 400 == 0):
   print(f"El año {año} es bisiesto")
else:
   print("No es un año bisiesto")
   

"""
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingrese su edad: "))
if edad >=0 and edad<=2:
   print("ere un bb")
elif edad >= 3 and edad <=12:
   print("Niño")
elif edad >=13 and edad <=17:
   print("Adolescente")
elif edad >= 18 and edad<= 64:
   print("Adulto")
elif edad >=65 :
   print("Adulto mayor")
else:
   print("El numero ingresado no es valido")
