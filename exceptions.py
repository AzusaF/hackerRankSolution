# Exceptions
numTests = int(input())
for i in range(numTests):
  values = input().split()
  try:
      print(int(values[0])//int(values[1]))
  except ValueError as e:
      print("Error Code:",e)
  except ZeroDivisionError as e:
      print("Error Code:",e)
