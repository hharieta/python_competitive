from statistics import median
n = int(input())
entrada = list(map(int, input().split()))

print(median(entrada), entrada.index(median(entrada)))

