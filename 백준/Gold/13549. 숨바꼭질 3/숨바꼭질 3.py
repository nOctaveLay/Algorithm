from collections import deque
import sys
input=sys.stdin.readline
start,end=map(int,input().split())

# 메모리 제한 512MB, 시간 제한 2초

q = deque()
q.append(start)
dp = [0 for _ in range(100002)]
dp[start] = 0
while q:
    current_p = q.popleft()
    if current_p == end:
        print(dp[current_p])
        break
    for next_p in [current_p * 2, current_p-1, current_p+1]:
        # next_p의 유효성 검사
        if next_p > 100000 or next_p < 0: continue
        if dp[next_p] : continue

        if next_p == current_p * 2:
            dp[next_p] = dp[current_p]
        else:
            dp[next_p] = dp[current_p] + 1
        q.append(next_p)