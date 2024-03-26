# Collections.OrderedDict()

from collections import OrderedDict
d = OrderedDict()

for _ in range(int(input())):
    item, separator, price = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(price)

for item, total in d.items():
    print(item, total)
