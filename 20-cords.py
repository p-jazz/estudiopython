size = int(input("¿De que tamaño quieres el cuadrante: ?")) # size == talla
# row == fila
# col == columna

for row in range(size):
    line = ""
    for col in range(size):
        line += f"({row},{col})"
    print(line)
    