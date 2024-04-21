# The Captain's Room

K = int(input())
roomNumbers = list(map(int, input().split()))

unique = set()
multiple = set()

for roomNumber in roomNumbers:
  if roomNumber not in unique:
    unique.add(roomNumber)
  else:
    multiple.add(roomNumber)
    
print(unique.difference(multiple).pop())
