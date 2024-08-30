import sys

def clean_the_room(cx,cy,d):
    global cnt
    # cleansing
    if arr[cx][cy] == 0:
        cnt += 1
        arr[cx][cy] = 2    
    for _ in range(4):
        # 왼쪽 방향으로 돌리기.
        nd = (d+3) % 4
        # 왼쪽으로 이동했을 때의 x,y값
        rx,ry = cx + dx[nd], cy + dy[nd]
        if arr[rx][ry] == 0:
            clean_the_room(rx,ry,nd)
            return
        # 만약에 왼쪽으로 이동 못했을 경우 다시 왼쪽으로 회전
        d = nd

    # 후진
    # 후진을 할 때에는 왼쪽으로 돌리기 전 방향으로 후진해야 한다.
    rx,ry = cx - dx[d], cy - dy[d]
    if arr[rx][ry] == 1:
        return
    else:
        clean_the_room(rx,ry,d)


if __name__ == "__main__":
    
    input = sys.stdin.readline

    n, m = map(int,input().split())
    r, c, d = map(int,input().split())

    dx = [-1,0,1,0] # 북 동 남 서
    dy = [0,1,0,-1]

    # 1 : 벽, 0 : 빈칸
    arr = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0

    clean_the_room(r,c,d)
    print(cnt)