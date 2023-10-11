from sys import stdin, stdout
import heapq 

# Equipo, Enemigos = map(int, stdin.readline().split())

# nombres_enemigos = list(map(str, stdin.readline().split()))
# datos = []
# nombres_disponibles = []
# energia_disponibles = []

# for nombre in range(Equipo):
#     n = input().split()
#     if int(n[2]) > 0:
#         nombres_disponibles.append(n[0])
#         energia_disponibles.append(n[1])

# mayor_sinergia = heapq.nlargest(Enemigos, energia_disponibles)
# nombres_seleccionados = []

# for m in range(mayor_sinergia.__len__()):
#     nombres_seleccionados.append(nombres_disponibles[energia_disponibles.index(mayor_sinergia[m])])

# nombres_seleccionados.sort()
# for nombre in nombres_seleccionados:
#     print(nombre)
    
Equipo, Enemigos = map(int, stdin.readline().split())

nombres_enemigos = list(map(str, stdin.readline().split()))
datos = []
nombres_disponibles = []
energia_disponibles = []

for nombre in range(Equipo):
    n = input().split()
    nombres_disponibles.append(n[0])
    energia_disponibles.append(n[1])

mayor_sinergia = heapq.nlargest(Enemigos, energia_disponibles)
nombres_seleccionados = []

for m in range(mayor_sinergia.__len__()):
    nombres_seleccionados.append(nombres_disponibles[energia_disponibles.index(mayor_sinergia[m])])

nombres_seleccionados.sort()
for nombre in nombres_seleccionados:
    print(nombre)