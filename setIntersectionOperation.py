# Set .intersection() Operation

numEn = int(input())
enStu = set(map(int, input().split()))

numFr = int(input())
frStu = set(map(int, input().split()))

print(len(enStu.intersection(frStu)))
