import heapq
from sys import stdout


# Python code to find 3 largest and 4 smallest
# elements of a list.
grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]

stdout.write(heapq.nlargest(3, grades).__str__())
stdout.write(heapq.nsmallest(3, grades).__str__())