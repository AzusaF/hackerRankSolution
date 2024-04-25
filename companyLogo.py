# Company Logo

from collections import Counter

if __name__ == '__main__':
  for key , value in Counter(sorted(input())).most_common(3):
    print(key, value)
