import sys

def dfs(current,start,num_of_direction):
    
    global check
    cx, cy = current
    sx, sy = start
    if check: return
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if (nx >= n or nx < 0) or (ny >= m or ny < 0) : continue
        if num_of_direction >= 4 and current == start:
            check = True
            return
        if not visited[nx][ny] and arr[nx][ny] == arr[sx][sy]:
            visited[nx][ny] = 1
            dfs((nx,ny),start,num_of_direction+1)
            visited[nx][ny] = 0

def find_cycle():
    global check
    for i in range(n):
        for j in range(m):
            dfs((i,j),(i,j),1)
            visited[i][j] = 1
            if check : return "Yes"
    return "No"

if __name__ == "__main__":
    input = sys.stdin.readline
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    check = False
    print(find_cycle())