# No Idea!

n, m = input().split()

C = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for num in C:
  if num in A:
    happiness += 1
  elif num in B:
    happiness -= 1
    
print(happiness)
