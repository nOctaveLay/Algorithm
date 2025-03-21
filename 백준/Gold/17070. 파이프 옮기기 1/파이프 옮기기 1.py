import sys
input = sys.stdin.readline



n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
# 가로 0, 세로 1, 대각선 2
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] #dp[x,y,z][0][0] = 0,0의 이전 파이프가 가로 개수 (x), 세로 개수(y), 대각선 개수(z)


# 첫 행에는 가로 파이프만 가능
dp[0][0][1] = 1 
for i in range(2,n):
    if arr[0][i] == 0:
        # 가로방향 update
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n): # 행
    for j in range(1,n): #열 (첫 열은 파이프의 이전 단계가 존재하지 않음.)
        # 대각선 방향 설치
        if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        
        # 가로 / 세로 방향 설치
        if arr[i][j] == 0:
            # 가로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]

            # 세로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

    
print(sum(dp[i][n-1][n-1] for i in range(3)))