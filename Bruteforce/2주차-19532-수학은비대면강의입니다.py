import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())

x = round((e*c-b*f)/(a*e-b*d))
y = round((-d*c+a*f)/(a*e-b*d))

print(x, y)