if __name__ == '__main__':
  # n = int(input())
  # integer_list = map(int, input().split())
  n = int(input())
  nums = input()

  l_str = nums.split( )

  l_int = list()
  for i in range(n):
    l_int.append(int(l_str[i]))

  t = tuple(l_int)
  print(hash(t))
