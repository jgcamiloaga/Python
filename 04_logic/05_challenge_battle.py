"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

# Fuerza bruta: buscar la solución A SACO.
# Algoritmos ocultos o cálculos o fórmulas
# Programación dinámica: buscar una solución mas eficiente


# def battle(lista_a, lista_b) :
#     a = lista_a [:]
#     b =lista_b [:]
#     diferencia = 0
#     ganador = None
#     for i in range(len(a)):
#         if a [i] > b [i]:
#             diferencia = a [i]- b[i]
#             if (i + 1) < len(a):
#                 a [i+1] += (diferencia)
#             ganador = "a"
#             ultima_diferencia = diferencia    
#         elif b [i] >a [i]:
#             diferencia =  b[i] - a[ i]
#             if (i +1) < len(b):
#                 b [i +1] +=(diferencia)
#             ganador = "b"
#             ultima_diferencia = diferencia    
#         else:
#             ganador = None
#             diferencia = 0
#     if ganador is None :
#         return "x"
#     else:
#         return f"{diferencia}{ganador}"      

# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]

# resultado = battle(lista_a, lista_b)  # -> "2b"
# print(battle(lista_a, lista_b))

def battle(lista_a, lista_b):
    puntos_a = sum(lista_a)
    puntos_b = sum(lista_b)
    return f"{puntos_a - puntos_b}a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}b" if puntos_b > puntos_a else "x"


lista_a = [2, 4, 2]
lista_b = [3, 3, 4]
winner = battle(lista_a, lista_b)
print(winner)