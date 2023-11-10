entrada = list(map(int, input().split()))

A = entrada[0]
B = entrada[1]
C = entrada[2]

gato1 = abs(C-A)
gato2 = abs(C-B)

if gato1 == gato2:
    print("raton C")
elif gato1 < gato2:
    print("gato A")
else:
    print("gato B")
