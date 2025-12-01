import sys

input = sys.stdin.readline
n = int(input())

min_time = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        min_time = min(min_time,b)
print(-1 if min_time == 1001 else min_time)