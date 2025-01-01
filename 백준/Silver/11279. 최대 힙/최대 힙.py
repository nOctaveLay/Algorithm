import sys
import heapq
input=sys.stdin.readline
n=int(input())
data=[]
for _ in range(n):
    cmd=int(input())
    if cmd == 0:
        if len(data) == 0: print(0)
        else: print(heapq.heappop(data)[1])
    else:
        heapq.heappush(data,(-cmd,cmd))