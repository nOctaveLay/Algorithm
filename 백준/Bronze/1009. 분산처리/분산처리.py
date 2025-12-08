import sys

input= sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    k = 1
    for i in range(b):
        k *= a % 10
        if k > 10:
            k = k % 10
    print(k if k != 0 else 10)