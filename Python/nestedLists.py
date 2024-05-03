# Nested Lists
if __name__ == '__main__':
  records = []
  for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    
records.sort(key=lambda score: score[1])

lowestScore = records[0][1]
i = 0

while records[i][1] == lowestScore:
  i += 1
secondLowestScore = records[i][1]

recordsToPrint = []
while i < len(records) and records[i][1] == secondLowestScore:
  recordsToPrint.append(records[i][0])
  i += 1

if len(recordsToPrint) > 1:
  recordsToPrint.sort()

for record in recordsToPrint:
  print(record)
