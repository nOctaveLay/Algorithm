import sys
sys.setrecursionlimit(10**6+20)
# dp[idx] : idx부터 시작하여, 최소 제곱의 합을 구함.
def solution(idx: int):
    # end condition
    if idx == n-1: # 모든 경우의 수 확인
        return 0 # 마지막 줄의 공백은 세지 않는다.
    
    # memorization 메모이제이션 
    if dp[idx] != max_value:
        return dp[idx]

    # 이 줄에 계속 쓸 경우
    left_space = m - arr[idx]
    for next_index in range(n):
        # 끝까지 다 썼다면
        if next_index == n-1:
            dp[idx] = 0
            break
        # 이 줄에서 분기할 경우
        dp[idx] = min(dp[idx], left_space * left_space + solution(next_index))
        left_space -= arr[next_index] + 1
        if left_space < 0:
            break

    return dp[idx]


if __name__ == "__main__":
    n, m = map(int, input().split())
    max_value = 1001
    dp = [max_value for _ in range(n)]
    dp[-1] = 0
    arr = list(int(input()) for _ in range(n))
    print(solution(0))
