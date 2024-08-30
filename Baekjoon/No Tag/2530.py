import sys
input = sys.stdin.readline
h,m,s = tuple(map(int,input().split()))
later_sec = int(input())
later_sec += s

m += later_sec // 60
s = later_sec % 60
h += m // 60 
print(h % 24, m % 60, s % 60, end = '')