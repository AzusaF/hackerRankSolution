# Collections.deque()

from collections import deque
numOfOperation = int(input())
d = deque()
for _ in range(numOfOperation):
  command = input().split()
  if command[0] == "append":
    d.append(int(command[1]))
  elif command[0] == "appendleft":
    d.appendleft(int(command[1]))
  elif command[0] == "clear":
    d.clear()
  elif command[0] == "extend":
    d.extend(int(command[1]))
  elif command[0] == "extendleft":
    d.extendleft(int(command[1]))
  elif command[0] == "count":
    d.count(int(command[1]))
  elif command[0] == "pop":
    d.pop()
  elif command[0] == "popleft":
    d.popleft()
  elif command[0] == "remove":
    d.remove(command[1])
  elif command[0] == "reverse":
    d.reverse()
  elif command[0] =="rotate":
    d.rotate(int(command[1]))

print(" ".join(str(item) for item in d))
