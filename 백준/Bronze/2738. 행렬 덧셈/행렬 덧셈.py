import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arrA = [list(map(int,input().split())) for _ in range(n)]
arrB = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(arrA[i][j] + arrB[i][j], end=' ')
    print()