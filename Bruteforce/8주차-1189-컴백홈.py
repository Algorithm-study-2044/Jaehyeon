from sys import stdin
R, C, K = map(int,stdin.readline().split())
arr = []
for _ in range(R):
    arr.append(list(stdin.readline()))
global ans
ans = 0

def DFS(row, col, u, d, l, r):
    if arr[row][col] =='T':
        return
    arr[row][col] = 'T'
    global ans
    if u == 0 and d==0 and l==0 and r==0:
        ans += 1
    if row>0 and u>0:
        DFS(row-1, col, u-1, d, l, r)
    if row<R-1 and d>0:
        DFS(row+1, col, u, d-1, l, r)
    if col>0 and l>0:
        DFS(row, col-1, u, d, l-1, r)
    if col<C-1 and r>0:
        DFS(row, col+1, u, d, l, r-1)
    arr[row][col] = '.'

if (K-C-R+1)%2 == 1 or K-C-R+1<0:
    print(0)
else:
    tot = (K-C-R+1)//2
    for left in range(tot+1):
        down = tot-left
        right = left+C-1
        up = down+R-1
        DFS(R-1, 0, up, down, left, right)
    
    print(ans)