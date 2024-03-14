def countmax(line):
    countarr = [1]
    for idx in range(1, len(line)):
        if line[idx-1] == line[idx]:
            countarr.append(countarr[-1]+1)
        else:
            countarr.append(1)
    return max(countarr)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

maxcandy = 0

for i in range(n):
    if i>0:
        for j in range(n):
            tmp = arr[i-1][j]
            arr[i-1][j] = arr[i][j]
            arr[i][j] = tmp
            res = countmax(arr[i])
            if maxcandy < res:
                maxcandy = res
            tmp = arr[i-1][j]
            arr[i-1][j] = arr[i][j]
            arr[i][j] = tmp
    if i<n-1:
        for j in range(n):
            tmp = arr[i+1][j]
            arr[i+1][j] = arr[i][j]
            arr[i][j] = tmp
            res = countmax(arr[i])
            if maxcandy < res:
                maxcandy = res
            tmp = arr[i+1][j]
            arr[i+1][j] = arr[i][j]
            arr[i][j] = tmp
    for j in range(1, n):
        tmp = arr[i][j-1]
        arr[i][j-1] = arr[i][j]
        arr[i][j] = tmp
        res = countmax(arr[i])
        if maxcandy < res:
            maxcandy = res
        tmp = arr[i][j-1]
        arr[i][j-1] = arr[i][j]
        arr[i][j] = tmp

for j in range(n):
    if j>0:
        for i in range(n):
            tmp = arr[i][j-1]
            arr[i][j-1] = arr[i][j]
            arr[i][j] = tmp
            res = countmax([arr[i][j] for i in range(n)])
            if maxcandy < res:
                maxcandy = res
            tmp = arr[i][j-1]
            arr[i][j-1] = arr[i][j]
            arr[i][j] = tmp
    if j<n-1:
        for i in range(n):
            tmp = arr[i][j+1]
            arr[i][j+1] = arr[i][j]
            arr[i][j] = tmp
            res = countmax([arr[i][j] for i in range(n)])
            if maxcandy < res:
                maxcandy = res
            tmp = arr[i][j+1]
            arr[i][j+1] = arr[i][j]
            arr[i][j] = tmp
    for i in range(1, n):
        tmp = arr[i-1][j]
        arr[i-1][j] = arr[i][j]
        arr[i][j] = tmp
        res = countmax([arr[i][j] for i in range(n)])
        if maxcandy < res:
            maxcandy = res
        tmp = arr[i-1][j]
        arr[i-1][j] = arr[i][j]
        arr[i][j] = tmp

print(maxcandy)