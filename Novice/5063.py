import sys
input = sys.stdin.readline
n = int(input())
ad = "advertise"
no_ad = "do not advertise"
no_diff = "does not matter"
for _ in range(n):
    r, e, c = map(int,input().split())
    if r > (e - c): print(no_ad)
    elif r == (e-c) : print(no_diff)
    else: print(ad)