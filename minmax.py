### 11672. Mínimo y máximo en un intervalo ###
from sys import stdin, stdout

NUMBERS, QUERIES = map(int, stdin.readline().split())

N = list(map(int, stdin.readline().split()))

for query in range(QUERIES):
    type_query, i, j = stdin.readline().split()

    if type_query == "C":
        stdout.write([min(N[int(i)-1: int(j)]), max(N[int(i)-1: int(j)])].__str__()[:])
    
    if type_query == "A":
        N[int(i)-1] = int(j)

