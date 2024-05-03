# itertools.combinations()
from itertools import combinations
inputs = input().split()
for i in range(int(inputs[1])):
  results = list(combinations(sorted(inputs[0]),i+1))
  for result in results:
    print("".join(result))
