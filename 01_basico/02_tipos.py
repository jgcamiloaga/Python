#Python tiene varios tipos de datos
#int, float, coaplex, str, bool, NoneType, list,tuple,dict,range,set...

"""
hikaaaaaaaaaaaaaaaaaaa
"""
#print("int:")
#print (type(10))
#print(type(0))
#print(type(-5))
#print(type(3456789778976544798778987))

print("float:")
print(type(3.24))
print(type(1e3))

num1=10*10*10
print(num1)
print(type(num1))

num2 = 1e3
print(num2)
print(type(num2))

#ausencia de valor
print("NoneType")

#Pedir el nombre al usuario y imprimirlo en un mensaje
nom = input ("Escriba su nombre ")
print("Bienvenido "+ nom )
#Pedir la edad a dos usuarios y mostrar la suma de las edades
nom1= int( input("Edad de la primera persona "))
nom2= int (input("Edad de la segunda persona "))
print(nom1+nom2)

#Pedir el pesos de dos usuarios y mostrar la suma de los pesos
peso1= float(input("Peso de la primera persona"))
peso2= float(input("Peso de la segunda persona"))
print("La suma de sus pesos es: ",(peso1+peso2))
