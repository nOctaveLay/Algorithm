import sys
input = sys.stdin.readline
def IsCross(sx,sy,arr):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    counter = 0
    # 중심 좌표에서 상하좌우를 확인한 뒤, d를 늘려서 상하좌우를 확인한다.
    while True:
        for i in range(4):
            nx,ny = sx + dx[i]*counter, sy + dy[i]*counter
            if not (0<=nx<n) or not(0<=ny<m): continue
            if arr[nx][ny] == '.':
                return counter-1
        if counter > max(n,m): return counter-1
        counter += 1

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = [list(input().rstrip("\n")) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                k = IsCross(i,j,arr)
                if k:
                    for l in range(1,k+1):
                        result.append([i+1,j+1,l])
                        
    for elem in result:
        print(*elem)