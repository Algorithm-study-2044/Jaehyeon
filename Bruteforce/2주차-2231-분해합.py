def f(N):
    n = len(str(N))
    for m in range(max(N-9*n,1), N):
        r = sum(list(map(int, list(str(m)))))
        if m+r == N:
            return m
    return 0

N = int(input())
print(f(N))