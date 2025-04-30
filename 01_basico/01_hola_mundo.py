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

