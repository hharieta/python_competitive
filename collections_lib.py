from collections import Counter
from sys import stdout

# Code to find top 1 elements and their counts
# using most_common

arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]

counter = Counter(arr)

top_three = counter.most_common(arr.__len__())

stdout.write(top_three.__str__())
