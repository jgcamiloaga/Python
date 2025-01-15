# 05 - Entrada de usuario (input())
# La función input permite obtener datos

nombre = input("Hola, como te llamas?\n");
print(f"Hola {nombre}, encantado de conocerte");

age = input("Cuantos años tienes?\n");
age = int(age);
print(f"Dentro de 20 años tendras {age + 20}");

# print("Obtener multiples valores a la vez\n");
pais, ciudad = input("En que país y ciudad vives?\n").split()
print(f"Tú vives en el país {pais} y en la ciudad {ciudad}")