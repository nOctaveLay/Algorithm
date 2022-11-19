from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

arr = [[int(c) for c in input().rstrip("\n")]for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]

def dfs():
    q = deque()
    init_position = (0,0)
    q.append(init_position)
    distance[0][0] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        tx,ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if distance[nx][ny] == 0 and arr[nx][ny] == 1:
                    distance[nx][ny] = distance[tx][ty] + 1
                    q.append((nx,ny))

dfs()
print(distance[n-1][m-1])


