# index start부터 index end까지 악수를 하는 경우의 수
# 굳이 모든 사람이 악수를 할 필요는 없다.
# 길이로 접근할 수 있을때 -> 길이로 접근하는 것도 하나의 방법이다.
# 항상 작은 단위부터 생각하자.
# 간단한 문젠데 #3일 걸림 # 다음엔 신중하게 풀기
def solution() -> int:
    
    # dp 초기화
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # 길이 1일때
    for i in range(1,n):
        dp[i][i+1] = int(arr[i-1] == arr[i])

    # 길이 2 이상일 때 
    for length in range(2,n):
        for i in range(1,n-length+1):
            dp[i][i+length] = dp[i+1][i+length-1] + int(arr[i-1] == arr[i-1+length])
            for k in range(length):
                dp[i][i+length] = max(dp[i][i+length], dp[i][i+k] + dp[i+k+1][i+length])
    
    return dp[1][n]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution())