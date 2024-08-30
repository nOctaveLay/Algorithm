import sys

def solution(a: int, b: int, c:int, two_days_ago_worker: int, one_days_ago_worker: int):
    # 종료 조건
    if a == alpha_list[0] and b == alpha_list[1] and c == alpha_list[2]:
        return True

    if dp[a][b][c][two_days_ago_worker][one_days_ago_worker]:
        return False
    dp[a][b][c][two_days_ago_worker][one_days_ago_worker] = True
    # A는 매일 일할 수 있다.
    if a < alpha_list[0]:
        worker[a+b+c] = 'A'
        if solution(a+1, b, c, one_days_ago_worker, 0):
            return True

    # 전날 일 안했다면 B도 일할 수 있어.
    if b < alpha_list[1]:
        if one_days_ago_worker != 1:
            worker[a+b+c] = 'B'
            if solution(a, b+1, c, one_days_ago_worker, 1):
                return True

    # 전전날과 전날 C가 일하지 않았다면 C도 일할 수 있어.
    if c < alpha_list[2]:
        if two_days_ago_worker != 2 and one_days_ago_worker != 2:
            worker[a+b+c] = 'C'
            if solution(a, b, c+1, one_days_ago_worker, 2):
                return True

if __name__ == "__main__":
    input = sys.stdin.readline
    s = input().rstrip("\n")
    alpha_list = [0, 0, 0]

    for c in s:
        if c == 'A':
            alpha_list[0] += 1
        elif c == 'B':
            alpha_list[1] += 1
        else:
            alpha_list[2] += 1

    '''
    dp[days][a][b][two_days_ago_worker][one_days_ago_worker]: 
        [days] 날에 근무할 수 있는지 없는지를 볼거야 (T/F)
        [a] 일동안 A가 일했고, [b] 일동안 B가 일했으며,
        이틀 전에 일한 사람은 [two_days_ago_worker]야,
        하루 전에 일한 사람은 [one_days_ago_worker]야.
        일한 사람은 A:0, B:1, C:1로 표기하기로 했어.
    '''
    dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
    worker = ['' for _ in range(len(s))]
    if solution(0,0,0,0,0): print(*worker,sep='')
    else: print(-1)