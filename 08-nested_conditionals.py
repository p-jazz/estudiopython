name = input ("Cuál estu nombre: ")
age = int(input("Dime tu edad: "))

print(f"Hola{name}")

if age >= 18:
    drink = input("Que quieres cerveza o vino\n")
    if(drink) == "cerveza":
        print("Aquí tienes tu cerveza")
    else:
        print("Aqui esta tu vino\n")
else:
    juice = input("Quieres jugo de frutilla o naranja")
    if(juice =="frutilla" or juice == "frutillas"):
        print("Acá tienes tu jugo de fresas")