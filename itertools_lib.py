from itertools import permutations
from sys import stdout

perm = permutations([1,2,3], 2)

for i in list(perm):
    stdout.write(str(i))