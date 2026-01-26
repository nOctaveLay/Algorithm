import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int,input().split()))
    a = 0
    min_value = 101
    for i in arr:
        if i%2 == 0:
            a += i
            if min_value > i:
                min_value = i
    print(a, min_value)
    