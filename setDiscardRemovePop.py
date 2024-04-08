# Set .discard(), .remove() & .pop()

numOfNums = int(input())
nums = set(map(int, input().split()))

numOfOperations = int(input())

for i in range(numOfOperations):
  command = input().split()
  if command[0] == "pop":
    nums.pop()
  else:
    getattr(nums,command[0])(int(command[1]))
  
print(sum(nums))
