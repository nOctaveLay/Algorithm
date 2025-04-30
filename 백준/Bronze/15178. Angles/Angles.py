import sys
input=sys.stdin.readline

n = int(input())

for _ in range(n):
    a1, a2, a3 = map(int,input().split())
    print(a1, a2, a3, "Check" if a1+a2+a3 != 180 else "Seems OK")