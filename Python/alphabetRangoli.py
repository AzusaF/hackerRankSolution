# Alphabet Rangoli
import string

def print_rangoli(size):
  for i in range(size-1, -1, -1):
    alpha = string.ascii_lowercase[size-1:i:-1]+string.ascii_lowercase[i:size]
    print("-".join(alpha).center(4*size-3, '-'))
  alpha = string.ascii_lowercase[size-1::-1]+string.ascii_lowercase[:size]
  for i in range(size-1):
    alpha = alpha.replace(chr(97+i),'').replace((chr(97+i+1)+chr(97+i+1)), chr(97+i+1))
    print("-".join(alpha).center(4*size-3, '-'))


if __name__ == '__main__':
  n = int(input())
  print_rangoli(n)
