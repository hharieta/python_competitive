n = input()
dulces = list(map(int, input().split()))
gema = input()

posibles = []

 
for dulce in dulces:
    if int(dulce) >= int(gema) - 3 and int(dulce) <= int(gema) + 3:
        if dulce not in posibles:
            posibles.append(dulce)


for p in posibles:
    print(p, sep=" ", end=" ")
print()