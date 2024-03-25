# Merge the Tools!

from textwrap import wrap

def unique_everseen(s):
  seen = ""
  for char in s:
    if char not in seen:
      seen = seen + char
  return seen
  
def merge_the_tools(string, k):
  sub_s = wrap(string, k)
  for i in range(len(sub_s)):
    print(unique_everseen(sub_s[i]))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
