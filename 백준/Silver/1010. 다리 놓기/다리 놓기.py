import sys

input=sys.stdin.readline
t = int(input())

def factorial(n,start=1):
    result = 1
    for i in range(start,n+1):
        result *= i
    return result

for _ in range(t):
    a,b = map(int,input().split())
    print(factorial(b,b-a+1)//factorial(a))
