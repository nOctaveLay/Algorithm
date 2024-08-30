from collections import deque
import sys
input = sys.stdin.readline

def bfs(mover_queue, water_queue):
    # 고슴도치는 물이 "이동할 곳" 으로 이동할 수 없다.
    # 즉, 물이 이동할 곳을 먼저 파악 -> 나중에 고슴도치 이동으로 해석할 수 있다.
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    

if __name__ == "__main__":
    r, c = map(int,input().split())
    arr = [list(input().split()) for _ in range(r)]
    mover_queue = deque()
    water_queue = deque()

    # queue 초기화
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'D':
                start = (i,j)
                mover_queue.append((i,j))
            elif arr[i][j] == 'S':
                end = (i,j)
            elif arr[i][j] == '*':
                water_queue.append((i,j))
