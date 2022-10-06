from collections import deque
import sys

def bfs(start):
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    distance = [[[0,0] for _ in range(m)] for _ in range(n)]
    distance[start[0]][start[1]][0] = 1
    q.append((start[0],start[1],0))
    while q:
        hr, hc, hwalls = q.popleft()
        if hr == n-1 and hc == m-1:
            return distance[hr][hc][hwalls]
        for i in range(4):
            nr, nc = hr + dx[i], hc + dy[i]
            if nr >= n or nr < 0 or nc >= m or nc < 0: continue
            if arr[nr][nc] == 0 and not distance[nr][nc][hwalls]:
                distance[nr][nc][hwalls] = distance[hr][hc][hwalls] + 1
                q.append((nr,nc,hwalls))
            elif hwalls == 0:
                distance[nr][nc][1] = distance[hr][hc][0] + 1
                q.append((nr,nc,1))
    return -1



if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    arr = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    print(bfs((0,0)))
