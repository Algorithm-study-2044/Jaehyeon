n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def f(arr, n):
    if n==1:
        return str(arr[0][0])
    else:
        arr1 = [arr[i][:n//2] for i in range(n//2)]
        arr2 = [arr[i][n//2:] for i in range(n//2)]
        arr3 = [arr[i][:n//2] for i in range(n//2, n)]
        arr4 = [arr[i][n//2:] for i in range(n//2, n)]
        res1 = f(arr1, n//2)
        res2 = f(arr2, n//2)
        res3 = f(arr3, n//2)
        res4 = f(arr4, n//2)
        if res1 == res2 == res3 == res4=='0':
            return '0'
        elif res1 == res2 == res3 == res4=='1':
            return '1'
        else:
            return '('+res1+res2+res3+res4+')'

print(f(arr, n))