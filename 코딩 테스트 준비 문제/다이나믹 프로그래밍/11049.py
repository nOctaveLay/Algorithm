import sys
def get_min_oper_num() -> int:
    max_value = 2**31 # 문제 참조.

    min_oper_dp = [[max_value for _ in range(n)] for _ in range(n)]
    for i in range(n):
        min_oper_dp[i][i] = 0

    for interval in range(1,n): # 곱하는 갯수
        for start in range(n-interval):
            end = start + interval
            for k in range(start,end): # 곱할 때 묶는 숫자
                min_oper_dp[start][end] = min(min_oper_dp[start][k] + min_oper_dp[k+1][end] + (arr[start][0] * arr[k][1] * arr[end][1]), min_oper_dp[start][end])
    return min_oper_dp[0][n-1]
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n)]
    print(get_min_oper_num())