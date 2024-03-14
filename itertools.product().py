# itertools.product()

from itertools import product

A = map(int,(input()).split( ))
B = map(int,(input()).split( ))

C = list(product(A, B))


print(" ".join(map(str, C)))
