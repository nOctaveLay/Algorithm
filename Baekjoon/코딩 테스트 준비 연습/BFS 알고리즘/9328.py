from collections import deque
def bfs(position, key):
    q = deque()
    q.append((position,key))
    d = [(1,0), (-1,0), (0,1), (0,-1)]
    max_value = 0
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if arr[nx][ny] == '.':
                q.append(((nx,ny),key))
            elif arr[nx][ny].islower():
                q.append((nx,ny), key.append(arr[nx][ny]))
            elif arr[nx][ny].isupper():
                if arr[nx][ny] in key:
                    q.append((nx,ny), key)
            else:

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(h)]
        key = list(input().rstrip("\n"))
        