import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

if a == b:
    if a == c:
        result = 10000 + a*1000
    else:
        result = 1000 + a * 100
elif a == c: # a != b and a = c
    result = 1000 + a * 100
elif b == c : # a != b, a !=c but b = c
    result = 1000 + b * 100
else:
    result = max(a,b,c) * 100

print(result,end = '')