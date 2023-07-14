# Hacer una función que imprima los números del 0 al n como parámetro

def print_nums(number):
    print("--------")
    for num in range(number+1):
        print(f"--{num}--")


print_nums(5)
print_nums(10)