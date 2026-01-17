import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = sorted(list(map(int,input().split())))
    if arr[-2] - arr[1] >= 4:
        print("KIN")
    else:
        print(sum(arr[1:-1]))
