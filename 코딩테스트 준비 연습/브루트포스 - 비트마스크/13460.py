# 6087에서 풀었던 것과 비슷한 형식이네
from collections import deque
import sys
input = sys.stdin.readline

# 마지막까지 공이 이동했을 때의 위치를 돌려준다.
def return_ball_position(x,y,move_position):
    while True:
        x, y = x + dx[move_position], y + dy[move_position]
        # 다음 이동 경로가 벽인 경우
        if arr[x][y] == '#':
            # 벽위치와 구슬의 위치는 같이 있을 수 없다.
            x -= dx[move_position]
            y -= dy[move_position]
            break
        # 다음 이동 경로가 구멍인 경우
        if arr[x][y] == 'O':
            break
    return (x,y)
    
            
def bfs(rs,bs):
    srx, sry = rs # 빨간 구슬
    sbx, sby = bs # 파란 구슬
    q = deque()
    q.append((0,srx,sry,sbx,sby))
    visited = []
    visited.append((srx,sry,sbx,sby))
    while q:
        level,rx,ry,bx,by = q.popleft()
        if arr[rx][ry] == 'O':
            print(level)
            return
        if level > 10:
            print(-1)
            return
        for i in range(4):
            # 양 구슬을 같은 방향으로 둘 다 안 움직일 때까지 움직임
            # 빨간 구슬을 끝까지 움직인다.
            nrx, nry = return_ball_position(rx,ry,i)
            # 파란 구슬을 끝까지 움직인다.
            nbx, nby = return_ball_position(bx,by,i)

            # 만약 파란 구슬이 구멍에 들어갔다면
            # 주의 : 파란구슬이 먼저 들어가든 나중에 들어가든 어쨌든 구멍엔 절대 들어가선 안됨
            if arr[nbx][nby] == 'O':
                continue

            # 빨간 구슬과 파란 구슬이 겹치면 안되므로
            if nrx == nbx and nry == nby:
                rcnt = abs(rx-nrx) + abs(ry-nry)
                bcnt = abs(bx-nbx) + abs(by-nby)
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            # 블루는 안 움직이고 레드만 움직일 때도 있으므로 
            if (nrx,nry,nbx,nby) not in visited:
                q.append((level+1,nrx,nry,nbx,nby))
                visited.append((nrx,nry,nbx,nby))
    print(-1)

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    rs, bs = (0,0), (0,0)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                rs = (i,j)
            elif arr[i][j] == 'B':
                bs = (i,j)
            else: continue
    bfs(rs,bs)