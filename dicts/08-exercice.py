# Escribir un archivo Python que genere e imprima un diccionario que contiene numeros entre 1 y n en la forma de {x: x*x}

user_option = int(input("Escribe un número: "))

dic = {}

for num in range(1, user_option + 1):
    dic[num] = num*num
print(dic)