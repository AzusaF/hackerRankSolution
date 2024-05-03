# Re.start() & Re.end()

S = input()
k = input()
import re
patternRegObj = re.compile(k)
r = patternRegObj.search(S)
if not r: print((-1, -1))
while r:
  print("(" + str(r.start()) + ", " + str(r.end() - 1) + ")")
  r = patternRegObj.search(S, r.start() + 1)
