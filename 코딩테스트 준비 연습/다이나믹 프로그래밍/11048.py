from sys import stdin
if __name__ == "__main__":
    input = stdin.readline
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)] # i,j로 이동했을 때 먹을 수 있는 사탕의 갯수
    
    # dp 초기화
    dp[0][0] = arr[0][0]
    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + arr[0][i]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + arr[i][j]
    print(dp[n-1][m-1])