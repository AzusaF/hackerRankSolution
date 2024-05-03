# DefaultDict Tutorial
size = input().split()

A, B = [], []
toPrint = []
for i in range(int(size[0])):
  A.append(input())

for j in range(int(size[1])):
  B.append(input())
  for i in range(int(size[0])):
    if B[j] == A[i]:
      toPrint.append(str(i+1))
  if len(toPrint) == 0:
    print("-1") 
  else:
    print(" ".join(toPrint))
    toPrint = []
