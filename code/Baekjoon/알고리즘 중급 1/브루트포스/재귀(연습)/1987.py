from collections import deque
import sys

def dfs(position:tuple, cnt:int):
    x, y = position
    global max_value
    if max_value < cnt:
        max_value = cnt
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not (0<=nx<r and 0<=ny<c): continue
        if arr[x][y] != arr[nx][ny] and not visited[ord(arr[nx][ny]) - ord('A')]:
            visited[ord(arr[nx][ny]) - ord('A')] = 1
            dfs((nx,ny),cnt+1)
            visited[ord(arr[nx][ny]) - ord('A')] = 0

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(r)]
    
    max_value = 0
    d = [(0,1),(0,-1),(1,0),(-1,0)]

    visited = [0 for _ in range(ord('Z')-ord('A') + 1)] # 0,0이니까 할 수 있는 테크닉
    visited[ord(arr[0][0]) - ord('A')] = 1

    dfs((0,0),1)
    print(max_value)