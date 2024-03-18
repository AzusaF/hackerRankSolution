# collections.Counter()

import collections

numOfShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numOfCustomer = int(input())

total = 0
for i in range(numOfCustomer):
  size, price = map(int, input().split())
  if shoes[size]:
    total += price
    shoes[size] -= 1

print(total)
