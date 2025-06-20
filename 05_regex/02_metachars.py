###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re

#1. El punto (.)
#coincidir con cualquier caracter excepto una nueva linea

text ="Hola mundo, H0la de nuevo, H$ola otra vez"
pattern = "H.la"#Hola,
found=re.findall(pattern,text)

if (found):
    print(found)
else:
    print("No se ha encontrado este patron")

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern,text)
print(matches)


#--------------------------------

text ="Hola mundo, H0la de nuevo, H$ola otra vez"
pattern = r"H.la"#Hola,
found=re.findall(pattern,text)

if (found):
    print(found)
else:
    print("No se ha encontrado este patron")


#Como usar la barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern= r"\."

matches = re.findall(pattern,text)

print(matches)

#\d: coincide con cualquier digito (0-9)

text="El numero de telefono es 123456789"
found= re.findall(r'\d{9}',text)

print(found)

#EJERCICIO : Detectar si hay un numero de españa en el texto gracias al perfijo +34
 
text = "Mi numero de telefono es +34 68899999999 apuntalo vale?"
pattern= r"\+34 \d{9}"
found =re.search(pattern,text)
if found: print(f" Encontre el numero de telefono {found.group()}")