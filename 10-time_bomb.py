import time

# EJERCICIO:Hacer un programa que parta contando regresivamente desde 10 y que al llegar a 0 diga "Boom"
# tip: esperar un segundo entre cada iteración utilizando time.sleep(1)

num = 10
while num >= 0:
    print(f"Esta es la vuelta número {num}")    
    num = num - 1
    time.sleep(1)
    
print("boom")
print(num) 