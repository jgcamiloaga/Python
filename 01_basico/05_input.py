# 05 - Entrada de usuario (input())
# La función input permite obtener datos



##Pedir información --input

print("Hola, ¿como te llamas?")
nombre = input()


nombre = input("Hola, como te llamas?\n")
print(f"Hola{nombre}, encantado de conocerte")## el f  es para poner un dato entero o flotante

age = input("¿cuantos años tienes?\n")
age= int(age)
print(f"Tiene {age+ 20} años")


print("Obtener multiples valores a la vez")
country,city, street = input("¿En que pais y ciudad vives?\n").split()
print(f"vives en {country},{city},{street}")


