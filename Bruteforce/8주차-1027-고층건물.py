from sys import stdin
n = int(stdin.readline())
heights = list(map(int, stdin.readline().split()))
available = [[True for _ in range(n)] for __ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        for k in range(i+1, j):
            if (j-k)*(heights[k]-heights[i]) >= (k-i)*(heights[j]-heights[k]):
                available[i][j] = False
                available[j][i] = False

seecnt = []
for arr in available:
    cnt = 0
    for flag in arr:
        if flag:
            cnt += 1
    seecnt.append(cnt)

print(max(seecnt)-1)