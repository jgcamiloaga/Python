import os as sistemaoperativo
sistemaoperativo.system("clear")

# Booleanos
print(True)
print(False)

# Operadores de comparación: devuelven un booleano
print("5 > 3: ", 5 > 3)
print("5 < 3: ", 5 < 3)
print("5 >= 3: ", 5 >= 3)
print("5 <= 3: ", 5 <= 3)
print("5 == 3: ", 5 == 3)
print("5 != 3: ", 5 != 3)

# Lexicográficamente
print("manzana < pera: ", "manzana" < "pera") # Que sale aquí? 

# Operadores lógicos
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and False: ", False and False)
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or False: ", False or False)
print("not True: ", not True)
print("not False: ", not False)

# Tablas de verdad (para referencia)
print("\nTablas de verdad")
print("and:")
print("A     B    A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\nor:")
print("A     B    A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\nnot:")
print("A     not A")
print("True  ", not True)
print("False ", not False)

