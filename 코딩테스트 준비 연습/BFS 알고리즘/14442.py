# python3로 불가능함 -> gc때문에 그런듯?
# 중복체크하지 않는 것은 매우 중요하다.
from collections import deque
import sys

def adj(k):
    i, j = k // m, k % m
    # 상
    if i > 0:
        yield k - m
    # 하
    if i < n-1:
        yield k + m
    if j > 0:
        yield k - 1
    if j < m-1:
        yield k + 1

def bfs(start):
    q = deque()
    distance = [[0 for _ in range(n*m)] for _ in range(k+1)]
    distance[0][start] = 1
    q.append((start,0))
    while q:
        h, hwalls = q.popleft()
        hr, hc = h // m, h % m
        if h == n*m-1:
            return distance[hwalls][h]
        for i in adj(h):
            if not distance[hwalls][i] and arr[i//m][i % m] == 0: # 비워져 있는 곳이라면
                distance[hwalls][i] = distance[hwalls][h] + 1 # 벽은 그대로이고 거리만 달라지는 정도.
                q.append((i,hwalls))
            elif hwalls < k and not distance[hwalls+1][i]: # 비워져 있지는 않은데, 벽을 뚫고 갈 수 있다면
                distance[hwalls+1][i] = distance[hwalls][h] + 1
                q.append((i,hwalls+1))
    return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int,input().split())
    arr = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    print(bfs(0))
