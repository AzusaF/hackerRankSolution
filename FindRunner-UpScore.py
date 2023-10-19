if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = sorted(list(arr))
    max = list[n-1]
    idx = n-2
    for i in range(n-1,0,-1):
        if max == list[i]:
            idx = i-1
        if list[idx] > list[i]:
            break
    print(list[idx])