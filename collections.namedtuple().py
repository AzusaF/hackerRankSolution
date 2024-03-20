# Collections.namedtuple()

from collections import namedtuple

numStudents = int(input())
Test = namedtuple('Test', ' '.join(input().split()))
total = 0
for i in range(1, numStudents+1):
  field1, field2, field3, field4 = input().split()
  test = Test(field1, field2, field3, field4)
  total += int(test.MARKS)
print(round(total/numStudents,2))
