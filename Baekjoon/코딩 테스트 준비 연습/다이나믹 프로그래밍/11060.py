from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [n+1 for _ in range(n)]
    dp[0] = 0
    for i in range(1,n):
        for k in range(i):
            if i <= k + arr[k]:
                dp[i] = min(dp[i], dp[k] + 1)
    print(dp[n-1] if dp[n-1] != n+1 else -1)