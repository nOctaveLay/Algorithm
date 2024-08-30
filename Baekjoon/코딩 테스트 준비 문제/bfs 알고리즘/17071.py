# 숨바꼭질 5 : https://www.acmicpc.net/problem/17071
from collections import deque
n, k = map(int, input().split())

def solution(subin_init:int, brother_init:int):
    q = deque()
    visited = [[-1, -1] for _ in range(500001)]
    q.append((subin_init,0))
    brother = brother_init
    visited[subin_init][0] = 0
    if subin_init == brother: return 0
    while q:
        nxt_q = deque()
        for _ in range(len(q)):
            subin, time = q.popleft()
            time += 1
            # subin 이동
            for next_subin in [subin - 1, subin + 1, subin * 2]:
                if next_subin < 0 or next_subin > 500000: continue
                if visited[next_subin][time % 2] > -1: continue
                nxt_q.append((next_subin, time))
                visited[next_subin][time % 2] = time
            if not q:
                q, nxt_q = nxt_q, deque()
        # brother 이동
        brother += time
        if brother > 500000: return -1
        if visited[brother][time % 2] >= 0:
            return time
    return -1
result = solution(n, k)
print(result)