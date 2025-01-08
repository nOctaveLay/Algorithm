import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

# 인접 리스트에 key로 값 집어넣기
def add_element(adjs:dict, key:int, value:int):
    if key not in adjs:
        adjs[key] = [value]
    else:
        adjs[key].append(value)
    return adjs

# 인접 행렬 -> 인접 리스트
adjs = dict()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            adjs = add_element(adjs,i,j)

# bfs 구현
def bfs(v:int):
    q = deque()
    q.append(v)
    visited = [0 for _ in range(n)]
    # visited[v] = 1
    while q:
        current_v = q.popleft()
        if current_v in adjs:
            # print(adjs[current_v])
            for next_v in adjs[current_v]:
                if not visited[next_v]:
                    visited[next_v] = 1
                    # print(visited)
                    q.append(next_v)
    return visited

# bfs로 하나씩 방문
for i in range(n):
    print(*bfs(i))
