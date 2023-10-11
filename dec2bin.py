from sys import stdin, stdout

count = 0
n = 0

def f(n):
    if n > 1:
        f(n/2)
    if n % 2 == 1:
        count += 1
    
    return count

n = list(map(int, stdin.readline().split()))
m = f(n[0])

print(m)