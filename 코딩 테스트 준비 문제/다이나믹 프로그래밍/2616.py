from itertools import accumulate

def solution():
    dp = [[0 for _ in range(n+1)] for _ in range(3)]
    for i in range(3):
        for j in range((i+1) * k , n+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + arr[j] - arr[j-k])

    return dp[2][-1]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    new_arr = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        new_arr[i] = arr[i-1] + new_arr[i-1]
    arr = new_arr
    k = int(input())
    print(solution())