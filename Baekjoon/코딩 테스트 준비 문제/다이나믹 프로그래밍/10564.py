import sys
def get_route(cnt,round):
    # dp[팔 굽혀펴기 횟수][round] : round마다 팔 굽혀펴기 횟수가 "팔 굽혀펴기 횟수"만큼 남았을 때의 가능한 점수의 최대값.
    # basic
    if cnt == 0:
        return 0

    # Memorization
    if dp[cnt][round] != -1: return dp[cnt][round]
    dp[cnt][round] = -1000000000
    # iterable
    for i in range(len(score)):
        if cnt - round * score[i] >= 0:
            dp[cnt][round] = max(dp[cnt][round], get_route(cnt - round * score[i], round + 1) + score[i])
    
    return dp[cnt][round]


if __name__ == "__main__":
    iter_num = int(input())
    for _ in range(iter_num):
        n, m = map(int, input().split())
        score = list(map(int, input().split()))
        dp = [[-1 for _ in range(201)] for _ in range(n+1)]
        result = get_route(n, 1)
        print(result if result > 0 else -1)