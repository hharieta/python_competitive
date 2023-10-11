from sys import stdin, stdout

def minimo_comun_divisor(n1: int, n2: int) -> int:
   if n2 == 0: return n1
   else: return minimo_comun_divisor(n2, (n1 % n2))


N = int(stdin.readline())

for i in range(N):
    n1, n2 = map(int, stdin.readline().split())

    stdout.write(("No primos\n", "Primos Relativos\n")[minimo_comun_divisor(n1, n2) == 1])
