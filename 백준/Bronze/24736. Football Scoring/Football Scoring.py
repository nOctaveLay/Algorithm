import sys

input = sys.stdin.readline

scores = [0,0]
for i in range(2):
    t,f,s,p,c = map(int,input().split())
    scores[i] = t*6+f*3+s*2+p+2*c

print(*scores)