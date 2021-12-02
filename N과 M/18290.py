import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -99999999

def checking(px,py,cnt,sum):
    if cnt == k:
        global answer

        if answer < sum:
            answer = sum

        return

    for x in range(px, n):
        for y in range(py if x==px else 0, m):

            # 현재 위치를 방문하지 않았다면
            if visited[x][y] == False:
                ok = True
                
                # 그리고 인근 위치 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                        if visited[nx][ny] == True:
                            ok = False
                
                if ok:
                    visited[x][y] = True
                    checking(x, y, cnt+1, sum+arr[x][y])
                    visited[x][y] = False

checking(0,0,0,0)

print(answer)