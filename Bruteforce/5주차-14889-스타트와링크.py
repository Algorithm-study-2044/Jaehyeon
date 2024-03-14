n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

from itertools import combinations

mindiff = 999999999999999999999999999999999999
totalset = set(range(n))

for subset in combinations(totalset, n//2):
    teamA = set(subset)
    teamB = totalset - teamA
    scoreA = 0
    scoreB = 0
    for i in teamA:
        for j in teamA:
            scoreA += arr[i][j]
    for i in teamB:
        for j in teamB:
            scoreB += arr[i][j]
    
    diff = abs(scoreA - scoreB)
    if mindiff > diff:
        mindiff = diff

print(mindiff)