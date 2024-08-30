from itertools import product
import sys

def solution(num_of_song:int, a_song:int, b_song:int, c_song:int) -> int:
    mod = 1000000007
    # end condition (종료 조건)
    if num_of_song == 0: # 더 이상 부를 곡이 남아있지 않다면
        if a_song == 0 and b_song == 0 and c_song == 0: # 만약 다 불렀다면
            return 1 # 이 경우의 수는 1
        else: 
            return 0 # 다 부르지 못했다면 그 경로가 완전한 것이 아님.
    
    # 메모이제이션
    if a_song < 0 or b_song < 0 or c_song < 0: 
        return 0 # 부를 곡들이 남았는데, 음수가 된다? 경로가 완전한 것이 아님
    if dp[num_of_song][a_song][b_song][c_song] != -1: 
        return dp[num_of_song][a_song][b_song][c_song]

    # 반복 조건
    dp[num_of_song][a_song][b_song][c_song] = 0
    for i,j,k in product(range(2), repeat = 3):
        if i + j + k == 0: continue
        dp[num_of_song][a_song][b_song][c_song] += solution(num_of_song - 1, a_song - i, b_song - j, c_song - k)
    dp[num_of_song][a_song][b_song][c_song] %= mod
    return dp[num_of_song][a_song][b_song][c_song]


if __name__ == "__main__":
    input = sys.stdin.readline
    S,a,b,c = map(int,input().split())
    dp = [[[[-1 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)] for _ in range(S+1)]
    print(solution(S,a,b,c))