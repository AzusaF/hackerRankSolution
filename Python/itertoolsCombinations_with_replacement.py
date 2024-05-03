# itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

string, size = input().split()

toPrint = list(combinations_with_replacement(sorted(string), int(size)))

for item in toPrint:
  print("".join(item))
