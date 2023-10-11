import heapq
from sys import stdout

stocks = {
    'Goog' : 520.54,
    'FB' : 76.45,
    'yhoo' : 39.28,
    'AMZN' : 306.21,
    'APPL' : 99.76
    }

# sorting according to values
zipped_1 = zip(stocks.values(), stocks.keys())
stdout.write(sorted(zipped_1).__str__())

#sorting according to keys
zipped_2 = zip(stocks.keys(), stocks.values())
stdout.write(sorted(zipped_2).__str__())
