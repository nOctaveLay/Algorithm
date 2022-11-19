# 엘레베이터 업치락 뒷치락
from collections import deque
import sys

def bfs(start):
    q = deque()
    q.append((start,0)) # 이거 문제 설명이 이상함.
    distance = [-1 for _ in range(f)]
    distance[start-1] = 0
    while q:
        here,cnt = q.popleft()
        if here == g:
            return cnt
        for i in [here + u, here -d]:
            if i > f or i < 1 : continue
            if distance[i-1] != -1 : continue # 만약 이미 방문한 지역이라면 굳이 더 진행할 필요는 없다.
            q.append((i,cnt+1))
            distance[i-1] = cnt + 1
    return "use the stairs"

if __name__ == "__main__":
    input = sys.stdin.readline
    f,s,g,u,d = map(int,input().split())
    print(bfs(s))