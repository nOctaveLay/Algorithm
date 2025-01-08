import sys
import heapq
input=sys.stdin.readline
n=int(input())
arr=[]

for _ in range(n):
    command = int(input())
    if command == 0:
        if len(arr) == 0 : print(0)
        else:
            x = heapq.heappop(arr)
            print(x[1])
    else:
        heapq.heappush(arr, (abs(command), command))
