#01 - print()
# El modulo print() es una función que imprime un mensaje en la pantalla.

print("Hola mundo !!")
print('Mostrar mensaje')

print("python","es","genial", sep="*") #espacio por defecto
print("python es genial", " 2")

print("Esto se imprime", end = "\n") #salto de linea
print("en una sola línea")

#Crea un programa que solicite al usuario ingresar un carácter separador.
#Luego, el programa debe imprimir cinco palabras separadas por el carácter ingresado.

a = input ("Ingrese un carácter separador: ")
print("uno ","dos ","tres ","cuatro ","cinco ", sep= a)

#Crea un programa que imprima tres líneas de texto, una palabra en cada línea.
#Antes de imprimir cada palabra, el programa debe preguntar al usuario qué 
#carácter desea utilizar al final de la línea (en lugar del salto de línea por defecto).

salto = input ("Ingrese el primer caracter: ")
salto1 = input ("Ingrese el segundo caracter: ")
salto2 = input("Ingrese el tercer caracter: ")
print("dana esta aprendiendo ", end = salto)
print(" dana esta escribiendo ", end = salto1)
print(" dana esta programando ",end = salto2)