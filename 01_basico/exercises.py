###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = input("Cómo te llamas?\n");
print(f"Tú te llamas {nombre}");
ciudad = input("En que ciudad vives?\n");
print(f"Tú vives en la ciudad {ciudad}");

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a));
print(type(b));
print(type(c));
print(type(d));
print(type(e));

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
var_cadena = "12345";
var_entero_1 = int(var_cadena);
print(type(var_entero_1));
print(var_entero_1)

var_flotante = 3.99;
var_entera_2 = int(var_flotante);
print(type(var_entera_2));
print(var_entera_2);
# SE IMPRIME EL NUMERO 3, ES DECIR, SE REDONDEA PARA ABAJO

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = "Johann";
edad = 21;
altura = 1.63;

print(f"Hola me llamo {nombre} y tengo {edad} años, mido {altura} metros");


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
import math
numero_1 = math.pi;
numero_2 = round(numero_1);
numero_3 = numero_2 // 2;
print(numero_3);
