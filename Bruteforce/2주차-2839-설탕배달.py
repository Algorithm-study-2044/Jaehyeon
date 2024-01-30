
def f(N):
    n5 = N//5
    r = N%5
    if r%3==0:
        n3 = r//3
        return n5+n3
    n5 -= 1
    if n5<0:
        return -1
    r+=5
    if r%3==0:
        n3 = r//3
        return n5+n3
    n5 -= 1
    if n5<0:
        return -1
    r+=5
    if r%3==0:
        n3 = r//3
        return n5+n3
    return -1


N = int(input())
print(f(N))