import sys
sys.setrecursionlimit(10**9)
def dfs(start,current_color):
    global ans
    sr, sc = start
    color_list[sr][sc] = current_color
    
    ans = max(ans,1)
    for i in range(6):
        nr, nc = sr + d[i][0], sc + d[i][1]
        if nr >= n or nr < 0 or nc >=n or nc < 0 : continue
        if arr[nr][nc] == 'X' :
            if color_list[nr][nc] == -1: # 아직 방문한 적이 없음. 
                dfs((nr,nc),1-current_color)
                ans = max(ans,2)
            elif color_list[nr][nc] == current_color: # 방문을 했고, 색을 칠했는데 이전 색이랑 같음?? => 완전 다른 색으로 칠해줘야 하는 유형임.
                print(3)
                exit()



if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [list(input().rstrip("\n")) for _ in range(n)]
    color_list = [[-1 for _ in range(n)] for _ in range(n)]
    d = {0:(-1,1),1:(0,1),2:(1,0),3:(1,-1), 4: (0,-1), 5:(-1,0)}
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X' and color_list[i][j] == -1:
                dfs((i,j),0)
    print(ans)