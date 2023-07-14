# Las expresiones booleanas nos permiten hacer flujo de ejecución condicional utilizando estructuras de control

age = int(input("¿Cuál es tu edad?\n"))

if (age >= 18): # El "if" no necesita ser ejecutado con ()
    print("Eres mayor de edad")

else:
    print("Entonces eres menor de edad")