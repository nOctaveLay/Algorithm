import sys
def gcd(a:int, b:int):
    while b != 0:
        a, b = b, a%b
    return a

def solution(num_of_boxes: int, num_of_bomb: int) -> int:
    # dp[i][j] : 상자가 i번째까지 있고, 폭탄이 j개 있을 때 상자를 열 수 있는 경우의 수
    dp = [[0 for _ in range(num_of_boxes+1)] for _ in range(num_of_boxes+1)]
    
    # dp 초기화, 상자가 1개 있고, 폭탄이 1개 있을 때가 가장 기본적인 단위이다.
    dp[1][1] = 1

    # iterable (i >= 2)
    for i in range(2,n+1): # 상자의 개수 및 번호
        for j in range(1,i+1): # 폭탄이 i개 있다 = 상자를 다 열 수 있다.
            dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]

    # 확률 계산
    all_case = sum(dp[n])

    # 폭탄이 주어졌을 때 총 경우의 수
    some_case = 0
    for i in range(1, num_of_bomb+1):
        some_case += dp[n][i]
    m = gcd(all_case, some_case)

    return f'{some_case//m}/{all_case//m}'
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    result = solution(n, m)
    print(result,end = '')