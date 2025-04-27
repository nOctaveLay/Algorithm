import sys
input=sys.stdin.readline

n = int(input())
k = 1
while n != 0:
    k *= n
    n -= 1
print(k)