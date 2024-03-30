# Set .union() Operation
numEng = int(input())
engStu = set(map(int, input().split()))

numFr = int(input())
frStu = set(map(int, input().split()))

print(len(engStu.union(frStu)))
