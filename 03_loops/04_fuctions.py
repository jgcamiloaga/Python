###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###
"""Definicion de una funcion

del nombre_de_la_funcion(parametro1,parametro2, ....);
#docstring
#cuerpo de la funcion 
return valor_de_retorno #oppcional


"""
#Ejemplo de una funcion para imprimir algo en consola
def saludar():
    print("Hola")

#Ejemplo de una funcion con parametro 
def saludar_a (nombre):
    print(f"Hola {nombre}")
    
saludar_a("dana")

#Funciones con mas parametros 
def sumar (a,b):
    suma =a+ b
    return suma
result =sumar (2,3)
print(result)

#Documentar las funciones con docstring
def restar (a,b):
    """Resta dos numeros y devuelve el resultado"""
    return a - b
print(restar.__doc__)
help(restar)

#parametros por defecto 
def multiplicar(a,b =2):
    return a * b
print(multiplicar(2))
print(multiplicar(2,3))


#Argumentos clave
def describir_persona(nombre,edad,sexo):
    print(f"Soy {nombre}, tengo {edad} años y {sexo}")

#Parametros posicionales 
describir_persona("Dana",20,"F")
describir_persona("mujer","mad",39)


#Argumentos por clave 
#Parametros nombrados
describir_persona(sexo="F", nombre="Dana",edad=20)
describir_persona(sexo="F", nombre="Dana",edad=20)


#Argumentos de longitud de variable (*arg):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma +=numero
    return suma

print(sumar_numeros(1,2,3,4,5))


#Argumentos de clave-valor variable (**hwargs):
def mostrar_informacion_de(**hwargs):
    for clave, valor in hwargs.items():
        print(f"{clave} : {valor}")

mostrar_informacion_de(nombre="Dana", edad=20 , sexo="F")
print("\n")
mostrar_informacion_de(name ="johan",edad=21, pais ="uruguay")
mostrar_informacion_de(nik="nds", es_sub =True, is_rich=True)
mostrar_informacion_de(super_name="felixcasa", es_nodo=True,gatos=40)