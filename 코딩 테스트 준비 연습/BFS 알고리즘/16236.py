from collections import deque
import sys

def bfs(sr,sc,body_size):
    d = [(-1,0),(0,-1), (0,1), (1,0)] #위 -> 왼쪽 -> 나머지 순으로 먹기 위함.
    q = deque()
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[sr][sc] = 0
    q.append((sr,sc))

    q2 = deque()
    while q:
        hr, hc = q.popleft()
        for dx,dy in d:
            nr, nc = hr + dx, hc + dy
            if not (0<=nr<n) or not (0<=nc<n): continue
            if distance[nr][nc] > -1 : continue
            if arr[nr][nc] <= body_size: # 내 몸보다 작다면 -> 지나갈 수 있음
                q.append((nr,nc))
                distance[nr][nc] = distance[hr][hc] + 1
                if arr[nr][nc] != body_size and arr[nr][nc] != 0: # 내 몸보다 완전 작고, 0이 아니면 먹어야 함.
                    q2.append((nr,nc,distance[nr][nc]))
    return deque(sorted(q2,key = lambda x : (x[2],x[0],x[1])))

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    body_size = 2
    result = 0
    # 초기 위치 잡기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                sr, sc = i,j
    cnt = 0
    while True:
        arr[sr][sc] = 0
        q = bfs(sr,sc,body_size)
        if not len(q):
            print(result)
            break
        nr,nc,d = q.popleft()
        result += d
        cnt += 1
        if cnt == body_size:
            cnt = 0
            body_size += 1
        sr,sc = nr,nc