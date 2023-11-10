from itertools import permutations


entrada = list(map(int, input().split()))
N = entrada[0]
K = entrada[1]

perm = permutations([n+1 for n in range(N)], K)

tmp = []
for i in list(perm):
    tmp.append(i)

output = []

sums = []

for tupla in tmp:
    sum = 0
    for n in tupla:
        sum += n
    if sum not in sums:
        output.append(tupla)
    sums.append(sum)
    sum = 0


# output = heapq.nsmallest(4, tmp)


for tupla in output:
    for num in tupla:
        print(num, end= " ")
    print()