# Check Subset

T = int(input())

for _ in range(T):
  numOfA = int(input())
  A = set(map(int, input().split()))
  numOfB = int(input())
  B = set(map(int, input().split()))
  
  print(A.issubset(B))
