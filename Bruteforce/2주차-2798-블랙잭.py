import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

max = 0
for i in range(N):
    sum1 = arr[i]
    if sum1>M:
        break
    for j in range(i+1, N):
        sum2 = sum1 + arr[j]
        if sum2>M:
            break
        for k in range(j+1, N):
            sum3 = sum2 + arr[k]
            if sum3>M:
                break
            if sum3>max:
                max = sum3

print(max)