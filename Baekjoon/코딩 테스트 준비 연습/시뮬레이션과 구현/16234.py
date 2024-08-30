# https://www.acmicpc.net/problem/16234
from collections import deque
import sys

def bfs(arr:list, visited:list, position:tuple, l:int, r:int, masking:int):
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    q = deque()
    q.append(position)
    visited[position[0]][position[1]] = masking
    count = 1
    sum_masking = arr[position[0]][position[1]]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny]: continue
            diff = abs(arr[x][y] - arr[nx][ny])

            if diff >= l and diff <= r:
                q.append((nx,ny))
                visited[nx][ny] = masking
                count += 1
                sum_masking += arr[nx][ny]
    return sum_masking // count

if __name__ == "__main__":
    n, l, r = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    people_num_dict = dict()

    cnt = 1
    days = 0
    check = 1
    while check:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    people_num = bfs(a,visited,(i,j),l,r,cnt)
                    people_num_dict[cnt] = people_num
                    cnt += 1
        check = 0
        for i in range(n):
            for j in range(n):
                cnt = visited[i][j]
                if a[i][j] != people_num_dict[cnt]:
                    a[i][j] = people_num_dict[cnt]
                    check = 1
        if check: days += 1
    print(days)