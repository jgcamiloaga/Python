#03 Casting de tipos
# Python permite convertir un tipo de dato a otro, esto se llama casting.

print("Conversiones de tipos de datos");
print(type(int("100")));

#Error de tipo de datos
# print(2 + "100"));

print( 5 + int("100"));

print( 5 + float("3.1416"));
print(int(3.1416));

print(bool(1));
print(bool(0));
print(bool(""));
print(bool("Hola"));
print(bool("False"));

print("100" + str(5));

print(int(2.5));