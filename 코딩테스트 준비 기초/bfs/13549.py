
from collections import deque
import sys

input = sys.stdin.readline
max_num = (10**5 + 1) * 2
start,end = map(int,input().split())

def bfs():
    taken_time = [-1] * max_num
    taken_time[start] = 0
    nvq = deque()
    nvq.append(start)
    while nvq:
        here = nvq.popleft()
        if here == end:
            print(taken_time[here],end = '')
            break
        for there in [here + 1, here - 1, here * 2]:
            if there >= 0 and there < max_num:
                if taken_time[there] == -1: # 방문하지 않았을 경우
                    if there != here * 2:
                        taken_time[there] = taken_time[here] + 1                
                        nvq.append(there)
                    else:
                        taken_time[there] = taken_time[here]
                        nvq.appendleft(there)
bfs()