# 04 - Variables
# Las variables son contenedores de datos. Un nombre simbólico que se refiere a un valor.

my_name = "Johann";
print(my_name);

age = 21;
print(age);

age = 22;
print(age);

# Tipado dinámico
# El tipo de dato de una variable puede cambiar durante la ejecución del programa
# No tienes que declarar explícitamente el tipo de dato de una variable

name = "Johann";
print(name);
print(type(name));

name = 21;
print(name);
print(type(name));

# Tipado Fuerte
# No puedes sumar un número con una cadena de texto
# Python es un lenguaje de tipado fuerte, no puedes cambiar el tipo de dato de una variable

print(f"Hola soy {my_name}, tengo {age} años");
print(f"La suma de los numeros: {name + 5}");

# No recomendada forma de asignar variables
name, age, city = "Johann", 21, "Lima";

#Convenciones de nombres de variables
mi_nombre_de_variable = "Johann"; #Snake Case
nombre = "Johann"; #Camel Case
MiNombreDeVariable = "Johann"; #Pascal Case
minimbredevariable = "Johann"; #Lower Case
MINOMBREDEVARIABLE = "Johann"; #Upper Case
mi_nombre_de_variable_123 = "Johann"; #Snake Case con numeros

MI_CONSTANTE = "Johann"; #Constante --> Upper case para las constantes

# ERROR 1111_nombre_de_variable = "Johann"; #No se puede iniciar con un numero
# ERROR nombre-de-variable = "Johann"; #No se puede usar guiones
# ERROR nombre de variable = "Johann"; #No se puede usar espacios
# ERROR class = "Johann"; #No se puede usar palabras reservadas

#Palabras reservadas

#[ 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' ]


is_user_logged_in: bool = True;
print(is_user_logged_in);

is_user_logged_in = 42;
print(is_user_logged_in);