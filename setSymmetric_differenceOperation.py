# Set .symmetric_difference() Operation
numEn = int(input())
enStu = set(map(int, input().split()))

numFr = int(input())
frStu = set(map(int, input().split()))

print(len(enStu.symmetric_difference(frStu)))
