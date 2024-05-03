# itertools.permutations()

from itertools import permutations

S = input().split( )
rc = list(permutations(sorted(S[0]), int(S[1])))
rc = ["".join(i) for i in rc]
print("\n".join(map(str, rc)))
