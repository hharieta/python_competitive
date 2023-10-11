import math

pasajeros = int(input())
habitacion_1 = int(input())

grupos = math.ceil(pasajeros / 3)
#print(grupos)
habitacion_final = habitacion_1

for i in range(1, grupos, 1):
    habitacion_final += 1

print(habitacion_final)