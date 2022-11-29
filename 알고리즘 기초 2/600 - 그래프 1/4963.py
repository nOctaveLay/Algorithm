from itertools import product
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
d = list(product([-1,0,1],repeat = 2))

def dfs(start):
    hx,hy = start
    for (dx,dy) in d:
        if not (dx == 0 and dy == 0):
            nx,ny = hx + dx, hy + dy
            if 0 <= nx < w and 0 <= ny < h:
                
                if arr[ny][nx] == 1:

                    arr[ny][nx] = 0
                    
                    dfs([nx,ny])

if __name__ == "__main__":
    while True:
        w, h = map(int,input().split())

        # 종료조건
        if w == 0 and h == 0:
            break
        arr = [list(map(int,input().split())) for _ in range(h)]
        count = 0    
        for j in range(w):
            for i in range(h):
                if arr[i][j] == 1:
                    arr[i][j] = 0
                    dfs([j,i])
                    count += 1
        print(count)