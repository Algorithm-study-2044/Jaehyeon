def f(n):
    s = str(n)
    l = len(s)
    for idx in range(l-2):
        if s[idx:idx+3] == '666':
            return True
    return False

N = int(input())
ans = 666
count = 0
while True:
    if f(ans):
        count += 1
    if count == N:
        print(ans)
        break
    ans += 1