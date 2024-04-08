# Set Mutations

numOfA = int(input())
A = set(map(int, input().split()))
numOfOperation = int(input())

for i in range(numOfOperation):
  command, new_elements = input().split()[0], set(map(int, input().split()))
  getattr(A, command)(new_elements)

print(sum(A))
