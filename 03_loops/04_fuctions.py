###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

# Ejercicio 1
def imprimir_numeros_del_1_al_10():
  for numero in range(1, 11):
    print(numero)

imprimir_numeros_del_1_al_10()

# Ejercicio 2
def imprimir_numeros_impares_del_1_al_20():
  for numero in range(1, 20, 2):
    print(numero)

imprimir_numeros_impares_del_1_al_20()

# Ejercicio 3
def imprimir_multiplos_de_5():
  for numero in range(5, 51, 5):
    print(numero)

imprimir_multiplos_de_5()

# Ejercicio 4
def imprimir_numeros_en_orden_inverso():
  for numero in range(10, 0, -1):
    print(numero)

imprimir_numeros_en_orden_inverso()

# Ejercicio 5
def sumar_numeros_del_1_al_100():
  suma = 0
  for numero in range(1, 101):
    suma += numero
  return suma

resultado = sumar_numeros_del_1_al_100()
print(resultado)

# Ejercicio 6
def tabla_de_multiplicar():
  numero = int(input("Introduce un número: "))
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

tabla_de_multiplicar()

# Ejercicio 7
def imprimir_mensaje(mensaje):
  print(mensaje)

imprimir_mensaje("Hola, soy un mensaje")

# Ejercicio 8
def sumar_dos_numeros(a, b):
  return a + b

resultado = sumar_dos_numeros(2, 3)
print(resultado)

# Ejercicio 9
def restar_dos_numeros(a, b):
  return a - b

resultado = restar_dos_numeros(5, 3)
print(resultado)

# Ejercicio 10
def multiplicar_dos_numeros(a, b=2):
  return a * b

resultado = multiplicar_dos_numeros(2)
print(resultado)

def sumar_numeros(a,b,c):
    return a + b + c

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

resultado = sumar_numeros(a, b, c)
print(resultado)