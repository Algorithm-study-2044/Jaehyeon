n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

from itertools import permutations

ans = 0
for a,b,c in permutations(range(1, 10), 3):
    flag = True
    for num, strike, ball in arr:
        a_ = num//100
        b_ = (num%100)//10
        c_ = num%10
        strike_ = 0
        ball_ = 0
        S = {a_, b_, c_}

        if a==a_:
            strike_ += 1
        if b==b_:
            strike_ += 1
        if c==c_:
            strike_ += 1
        
        if a in S:
            ball_ += 1
        if b in S:
            ball_ += 1
        if c in S:
            ball_ += 1
        
        ball_ -= strike_

        if ball != ball_ or strike != strike_:
            flag = False
            break
    if flag:
        ans += 1

print(ans)