###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

#Ejemplo tipico de diccionario
persona= {
    "nombre":"Dana",
    "edad":"20",
    "Es_estudiante": True,
    "calificaciones":[7,8,9],
    "social": {
        "twitter":"danam20",
        "instagram": "danamayuri",
        "facebook":"dana20"
    }
    }



#para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

#Cambiar valores al acceder
persona["nombre"]="Paloma"
persona["calificaciones"][2]=10

#eliminar completamente la propiedad
del persona["edad"]
print(persona)

es_estudiante =persona.pop("es_estudiante")
print(f"es_estudiante: (es_estudiante)")
print(persona)

#sobreescribir un diccionario con otro diccionario
a = {"name":"dana", "age":20}
b= {"name":"Paloma", "es_estudiante":True }

a.update(b)
print(a)

#Comprobar si existe una propiedad
print("name" in persona )#False
print("nombre" in persona )#true

#Obtener todas las clave
print("\nkeys:")
print(persona.keys())

#Obtener todos los valores
print("\nvalues:")
print(persona.values())

#Obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
    print(f"{key}:{value}")