
from collections import deque
import sys
# 플러드 필 알고리즘

def flood_fill(start,color):
    cnt = 1
    q = deque()
    q.append(start)
    arr[start[0]][start[1]] = color
    while q:
        hr, hc = q.popleft()
        for i in range(4):
            nr, nc = hr + dx[i], hc + dy[i]
            if nr >=n or nr < 0 or nc >= m or nc < 0: continue
            if not arr[nr][nc]:
                q.append((nr,nc))
                arr[nr][nc] = color
                cnt += 1
    return cnt

def move_(start):
    hr, hc = start
    group_set = set()
    for i in range(4):
        nr, nc = hr + dx[i], hc + dy[i]
        if nr >=n or nr < 0 or nc >= m or nc < 0: continue
        if arr[nr][nc] != 1:
            group_set.add(arr[nr][nc])
    cnt = 1
    for i in group_set:
        cnt += group_dict[i]
        cnt %= 10
    return cnt

color = 2
if __name__ == "__main__":
    
    input = sys.stdin.readline
    n, m = map(int,input().split())
    arr = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    group_dict = dict()
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                group_dict[color] = flood_fill((i,j),color)
                color += 1
    
    answer = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                answer[i][j] = move_((i,j))
    for elem in answer:
        print(*elem,sep='')