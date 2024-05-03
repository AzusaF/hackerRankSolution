# Compress the String!

from itertools import groupby

print(*((len(list(occurence)), int(num)) for num, occurence in groupby(input())))
