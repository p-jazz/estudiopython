# Recorrer el diccionario e imprimir cada estudiante de la siguiente forma

# El estuduante x reprobó con promedio y
# El estudiante x aprobó con promedio x

# La nota de aprobación la debe ingresar el usuario
user_option = float(input("Ingrese la nota de aprobación: "))
averages = {
    "Seba": 5,
    "Gaby": 6.5,
    "Fran": 7,
    "Jose": 6.4,
    "coni": 6.2,
    "Gonza": 4.8,
}

for student in averages.keys():
    if averages[student] > user_option:
        print(f"El estudiante {student} aprobo con promedio: {averages[student]}")
    else:
        print(f"El estudiante {student} reprobó con promedio: {averages[student]}")
    