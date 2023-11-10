entrada = list(map(int, input().split()))

a1, a2 = entrada[0], entrada[1]
b1, b2 = entrada[2], entrada[3]
c1, c2 = entrada[4], entrada[5]
d1, d2 = entrada[6], entrada[7]

n1 = a1 - b1
n2 = a2 - b2
m1 = c1 - d1
m2 = c2 - d2

print(n1, n2)
print(m1, m2)
if n1 == n2 and m1 == m2:
    print("Es válido")
    print(n1*n2)
else:
    print("No es válido")