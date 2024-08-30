from sys import stdin

input = stdin.readline

x,y,w,h = map(int,input().split())
answer = min(x,y,w-x,h-y)
print(answer,end='')