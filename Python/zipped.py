# Zipped!

numOfStudents, numOfSubjects = map(int, input().split()) 

sheet = []
for _ in range(numOfSubjects):
  sheet.append(map(float, input().split())) 

for score in zip(*sheet): 
  print(sum(score)/len(score))
