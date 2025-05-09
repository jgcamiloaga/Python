"""
print("\n Valores booleanos basicos")
print(True)
print(False)

#Operadores de comparacion: devuelven un valor booleanos
print("\nOPERADORES DE COMPARACION")
print("5 >3:", 5 > 3) #true
print("5 >3:", 5 > 3) #true
print("5 >3:", 5 > 3) #true
print("5 >3:", 5 > 3) #true
print("5 >3:", 5 > 3) #true
print("5 <= 3:", 5 <= 3) #true
"""

#Ejercicio 1: Sistema de calificación avanzado
#Escribe un programa que le pida al usuario su nota (de 0 a 100). Luego:
#Si la nota es mayor o igual a 90, imprimir "Excelente".
#Si está entre 80 y 89, imprimir "Muy bien".
#Si está entre 70 y 79, imprimir "Bien".
#Si está entre 60 y 69, imprimir "Suficiente".
#Si está entre 0 y 59, imprimir "Insuficiente".
#Si la nota no está en ese rango, imprimir "Nota no válida".

"""
nota = int(input("Ingrese su nota (0-100): "))
if nota >= 90 and nota<=100:
    print("Exelente")
elif nota >=80 and nota <=89:
    print("Muy bien")
elif nota >= 70 and nota <= 79:
    print("Bien")
elif nota >= 60 and nota <= 69:
    print("suficiente")
elif  nota >=0 and nota <= 59:
    print("Insuficiente")
else:
    print ("Nota no válida")

"""

#Ejercicio 2: Calculadora de tarifas
#Crea un programa que:
#Pida al usuario su edad y el día de la semana.
#Si el usuario tiene menos de 12 años o más de 65, el boleto cuesta $5.
#Si es fin de semana (sábado o domingo), cuesta $8.
#Si no, cuesta $10.
#Asegúrate de validar correctamente los datos ingresados.
"""
edad = int(input("Ingrese su edad: "))
diaSemana = input("Ingrese el dia: ").lower()# no importa min o mayusc
if edad < 12 or edad > 65:
    print("El boleto cuesta $5 ")
elif diaSemana == "sabado" or diaSemana=="domingo":
    print("El boleto cuesta $8")
elif diaSemana == "lunes" or diaSemana == "martes" or diaSemana == "miercoles" or diaSemana == "jueves" or diaSemana == "viernes":
    print("El boleto cuesta $10")
else:
    print("No es valido")
        
"""

#Ejercicio 3: Verificador de acceso
#Pide al usuario que introduzca:
#Su nombre de usuario.
#Su contraseña.
#Su rol (admin, editor, lector).
#Si el nombre de usuario y la contraseña son correctos (puedes fijar unos valores), y además:
#Si es admin, imprimir "Acceso total".
#Si es editor, imprimir "Acceso limitado".
#Si es lector, imprimir "Solo lectura".
#Si la contraseña o el usuario son incorrectos, imprimir "Acceso denegado".

#Usuario datos:
nom_usuario ="dan"
contra_usuario ="1234"
rol= "admin"

"""
#login
usuario = input("Ingrese su nombre: ")
contraseña = input("Escriba su contraseña: ")

if usuario == nom_usuario and contraseña== contra_usuario:
    if rol == "admin":
        print("Acceso total")
    elif rol == "editor":
        print("Acceso limitado")
    elif rol == "lector":
        print("Solo lectura")
    else:
        print("Rol no existe") 
else:
    print("Acceso denegado")
  """  
"""
for i in range(3):
    usuario = input("Ingrese su nombre: ")
    contraseña = input("Escriba su contraseña: ")
    if usuario == nom_usuario and contra_usuario == contraseña:
        
        print("datos correctos")

        if rol == "admin":
            print("Acceso total")
        elif rol == "editor":
            print("Acceso limitado")
        elif rol == "lector":
            print("Solo lectura")
        else:
            print("Rol no existe")
        break
    else:
        print("No existe")
else:
    print("A superado los 3 intentos máximos")


"""

#Ejercicio 4: Adivina el número
#El usuario debe ingresar un número del 1 al 100.
#Si el número es divisible por 3 y por 5, imprime “FizzBuzz”.
#Si solo es divisible por 3, imprime “Fizz”.
#Si solo es divisible por 5, imprime “Buzz”.
#Si no es divisible ni por 3 ni por 5, imprime el número.
#Si el número no está entre 1 y 100, imprime “Número fuera de rango”.
"""
numero = int(input("Ingresa un numero del 1 al 100: "))
if numero >=1 and numero <=100:
    if numero %3 ==0 and numero %5 == 0:
        print("FizzBuzz")
    elif numero %3 ==0:
        print("Fizz")
    elif numero %5 == 0:
        print("Buzz")
    elif numero %3 !=0 and numero %5 !=0:
        print(numero)
else:
    print("Fuera de rango")

    
#Solucion de johann
usuarioNumero = int(input("Ingrese un número del 1 al 100: "))
if usuarioNumero < 1 or usuarioNumero > 100:
    print("Número fuera de rango")
elif usuarioNumero % 3 == 0 and usuarioNumero % 5 == 0:
    print("FizzBuzz")
elif usuarioNumero % 3 == 0:
    print("Fizz")
elif usuarioNumero % 5 == 0:
    print("Buzz")
else:
    print(usuarioNumero)
    """
#Ejercicio 5: Evaluador de año bisiesto
#Solicita al usuario un año y determina si es bisiesto:
#Un año es bisiesto si es divisible por 4 y no por 100, o si es divisible por 400.
#Usa if, elif, else para tomar la decisión.
#Imprime si el año es o no bisiesto.

año = int(input("Ingrese el año: "))
if (año %4 ==0 and año %100 != 0) or(año %400 == 0):
    print( f"{año} es bisiesto")
else:
    print("no es un año bisiesto")
    #termino

    
    #DIFERENCIAS DEL GIT RESERT
    #git reset --soft HEAD~(n° de commit)
    #git reset --hard (id)
    #git push origin main --force #hard