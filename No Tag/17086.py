from collections import deque
from itertools import product
import sys
def return_deque_with_position_one(arr:list):
    q = deque()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                q.append((i,j))
    return q
    
def bfs(arr:list,q:deque):
    d = list(product([-1,0,1], repeat = 2))
    while q:
        hx, hy = q.popleft()
        for dx,dy in d:
            if dx == 0 and dy == 0: continue
            nx, ny = hx + dx, hy + dy
            if not (0 <= nx < len(arr)) or not (0 <= ny < len(arr[0])): continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[hx][hy] + 1
                q.append((nx,ny))
def return_max_value(arr:list):
    cnt = -1
    for rows in arr:
        row_max = max(rows)
        cnt = max(cnt,row_max)
    return cnt 

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    q = return_deque_with_position_one(arr)
    bfs(arr,q)
    print(return_max_value(arr)-1)
