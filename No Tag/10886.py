import sys
input = sys.stdin.readline
a,b = 0,0
n = int(input())
for _ in range(n):
    k = int(input())
    if k == 0 : a += 1
    else: b += 1

if a > b : print("Junhee is not cute!",end = '')
else: print("Junhee is cute!",end = '')