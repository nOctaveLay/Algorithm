from collections import deque
import sys

def bfs(sr,sc):
    # 모든 건물 안의 distance를 구해보자
    q = deque()
    distance = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    distance[sr][sc] = 0
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    q.append((sr,sc))
    while q:
        hr, hc = q.popleft()
        for dx,dy in d:

            nr, nc = hr + dx, hc + dy
            # 내가 가야할 곳이 범위 안에 제대로 있는지
            if not (0<=nr<h+2) or not(0<=nc<w+2): continue
            # 내가 이미 다녀갔던 곳인지 (backtracking x)
            if distance[nr][nc] != -1 : continue
            # 만약 내가 가야할 곳이 빈 공간이라면 (우선순위 높음)
            if arr[nr][nc] == '.' :
                distance[nr][nc] = distance[hr][hc] 
                q.appendleft((nr,nc))
            # 만약 내가 가야할 곳이 지나갈 수 없는 벽이라면 -> 아무것도 하지 않겠지.
            
            # 만약 내가 가야할 곳이 문이라면 (우선순위 낮음)
            elif arr[nr][nc] == '#':
                distance[nr][nc] = distance[hr][hc] + 1
                q.append((nr,nc))
    return distance

if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        h, w = map(int,input().split())
        # 추가하는 이유? 일일히 문의 위치를 찾기 귀찮아서.
        arr = deque(['.']+list(input().rstrip())+['.'] for _ in range(h)) # 열 추가
        arr.append(['.' for _ in range(w+2)]) # 행 위 추가
        arr.appendleft(['.' for _ in range(w+2)]) # 행 아래 추가

        start = []
        for i in range(h+2):
            for j in range(w+2):
                if arr[i][j] == '$':
                    start.append((i,j))
                    arr[i][j] = '.'

        # $이 아예 평면도에 안 들어가 있을 가능성도 있다. 왜 그런진 모르겠다. 이것때문에 index error남...;; 왜??
        if len(start) > 0:
            first = bfs(start[0][0],start[0][1])
        
        else: 
            first = bfs(0,0)

        if len(start) > 1:
            sec = bfs(start[1][0],start[1][1])
        else:
            sec = bfs(0,0)
        common = bfs(0,0)
        cnt =  10**6 + 1
        for i in range(h+2):
            for j in range(w+2):
                if first[i][j] == -1 or sec[i][j] == -1 or common[i][j] == -1: continue #공통 부분이 안생겼다는 의미
                else: 
                    the_num_of_door = first[i][j] + sec[i][j] + common[i][j]
                    if arr[i][j] == '#': # 자기 자리에 문이 있다면, 문을 3번 세게 되겠지
                        the_num_of_door -= 2
                    if cnt > the_num_of_door:
                        cnt = the_num_of_door
        print(cnt)