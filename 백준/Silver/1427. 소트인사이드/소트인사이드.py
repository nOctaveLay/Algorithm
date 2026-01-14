import sys

input = sys.stdin.readline

a = sorted(list(map(int,list(input().rstrip()))),reverse=True)
print(*a,sep='')