# Crear una función que retorne la suma de todos los numeros hasta el numero n pasado como parametro

user_option = int(input("Escribe un número: "))

def sum_up(number):
    total = 0
    for num in range(1, number + 1):
        total += num
    return total

print(sum_up(user_option))


