from collections import deque
import sys

# 섬에 각각 번호를 붙여준다.
# 1부터 시작하면 혼동이 있으므로, 2부터 붙여준다.
def make_island_name(position,count):
    q = deque()    
    q.append(position)
    arr[position[0]][position[1]] = count
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n): continue # 범위 조건
            if arr[nx][ny] == 1:
                arr[nx][ny] = count
                q.append((nx,ny))

def return_island_distance(island_name):
    
    distance = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == island_name:
                q.append((i,j))
                distance[i][j] = 1

    min_value = 999999
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n): continue # 범위 조건
            if distance[nx][ny] : continue # 이미 방문한 곳이면 더 이상 방문할 필요가 없다.
            if arr[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
            elif arr[nx][ny] != island_name:
                if min_value > distance[x][y]-1:
                    min_value = distance[x][y]-1

    return min_value

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    # island name 생성
    count = 2
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                make_island_name((i,j),count)
                count += 1

    # island 끼리의 거리 측정
    min_value = 999999
    for island_name in range(2,count):
        island_min_value = return_island_distance(island_name)
        if min_value > island_min_value:
            min_value = island_min_value

    print(min_value)