import heapq
import sys
input=sys.stdin.readline
n=int(input())
data = []
for _ in range(n):
    command = int(input())
    if command == 0:
        # 데이터가 없는데 출력하라고 한 경우
        if len(data) == 0 : print(0)
        else: print(heapq.heappop(data))
    else:
        heapq.heappush(data,command)