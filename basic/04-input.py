# Además de expulsar valores, datos o información , los programas reciben valores que de alguna forma manipulan y transforman. Python trae una función incorporada llamada "input" que permite ingresar datos o valores al programa.
print("Hola, dime cuál es tu nombre")
name = input()
print("Hola "+name)
print("¿Cuantos años tienes?")

# Una característica de la función "input" es que solo entrega texto.
age = int(input())
print(type(age)) # la función "print" trae un espacio

file_result = open('.hello.txt', 'w')
print("Naciste en",2023 - age, sep=": ", file=file_result) 

