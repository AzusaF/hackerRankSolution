# Iterables and Iterators

from itertools import combinations

N = int(input())
n = input().split()
K = int(input())
x = combinations(''.join(n), K)
count_total, count_a = 0, 0
for i in x:
  count_total += 1
  if 'a' in i:
    count_a += 1
print(round(count_a/count_total, 3))
