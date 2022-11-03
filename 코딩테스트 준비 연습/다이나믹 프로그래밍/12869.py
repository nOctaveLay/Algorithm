'''
Top - Down 방식의 DP.
dp[a][b][c] = 체력이 a, b, c 남았을 때 공격 횟수의 최솟값
'''
from itertools import permutations
import sys

# Top-Down 방식이 항상 어려운 것 같다.
def scv(a,b,c): #scv로 공격했을 때 남은 공격횟수.
    # 음수일 경우 0으로 바꿔준다.
    if a < 0 : a = 0
    if b < 0 : b = 0
    if c < 0 : c = 0
    
    # 종료 조건 만약 체력이 남아있지 않다면 공격할 이유가 없다.
    if a == 0 and b == 0 and c == 0: return 0

    # 중복 제거 (with memorization)
    if dp[a][b][c] != -1:
        return dp[a][b][c]

    dp[a][b][c] = 100
    for da, db, dc in permutations([-9,-3,-1]):
        dp[a][b][c] = min(dp[a][b][c], scv(a+da,b+db,c+dc) + 1)

    return dp[a][b][c]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    hp = list(map(int,input().split()))
    if len(hp) < 3:
        for i in range(3-len(hp)):
            hp.append(0)
    dp = [[[-1 for _ in range(hp[2]+1)] for _ in range(hp[1]+1)] for _ in range(hp[0]+1)]
    print(scv(*hp),end='')