from collections import deque
import sys

def bfs(coin):
    q = deque()
    q.append(coin)
    arr_row_max = len(arr)
    arr_column_max = len(arr[0])
    while q:
        c1r, c1c, c2r, c2c, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            n1r, n1c = c1r + dr[i], c1c + dc[i]
            n2r, n2c = c2r + dr[i], c2c + dc[i]
            if 0 <= n1r < arr_row_max and 0 <= n1c < arr_column_max: #coin1이 안 떨어진 경우
                if 0 <= n2r < arr_row_max and 0 <= n2c < arr_column_max: # coin2도 안 떨어진 경우
                    if arr[n1r][n1c] == '#':
                        n1r, n1c = c1r, c1c
                    if arr[n2r][n2c] == '#':
                        n2r, n2c = c2r, c2c
                    q.append([n1r,n1c,n2r,n2c,cnt+1])
                else:
                    return cnt + 1
            else: # coin1이 들어가버린경우
                if 0 <= n2r < arr_row_max and 0 <= n2c < arr_column_max: # coin2도 안 떨어진 경우
                    return cnt + 1
                #coin1도 들어가고, coin2도 들어간 경우 -> 아무 일도 일어나지 않음
    return -1

if __name__ == "__main__":
    
    input = sys.stdin.readline
    n, m = map(int,input().split())

    arr = [list(input().rstrip("\n")) for _ in range(n)]
    distance = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    temp = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'o':
                temp.append(i)
                temp.append(j)
    temp.append(0)
    print(bfs(temp))
