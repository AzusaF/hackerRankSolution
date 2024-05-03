# Symmetric Difference

sizeM = int(input())
setM = set(map(int, input().split()))

sizeN = int(input())
setN = set(map(int, input().split()))

difference = list(setM.difference(setN)) + list(setN.difference(setM))

for item in sorted(difference):
  print(item)
