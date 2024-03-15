from sys import stdin
n = int(stdin.readline())
arr = list(stdin.readline().split())

from collections import deque
maxq = deque([deque([0])])
minq = deque([deque([0])])

for idx, ineq in enumerate(arr):
    if ineq == '>':
        maxq.appendleft(deque([idx+1]))
        minq[-1].appendleft(idx+1)
    else:
        maxq[0].append(idx+1)
        minq.append(deque([idx+1]))

maxidx = []
minidx = []
for arr in maxq:
    for m in arr:
        maxidx.append(m)

for arr in minq:
    for m in arr:
        minidx.append(m)

maxarr = ['' for _ in range(n+1)]
minarr = ['' for _ in range(n+1)]

for idx in maxidx:
    maxarr[maxidx[idx]] = str(9-n+idx)
    minarr[minidx[idx]] = str(idx)

print(''.join(maxarr))
print(''.join(minarr))