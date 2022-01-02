from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for idx in idxs:
    find_index = dq.index(idx)
    if find_index < len(dq)/2:
        dq.rotate(-find_index)
        count += find_index
    else:
        dq.rotate(len(dq)-find_index)
        count += len(dq)-find_index
    dq.popleft()
    
print(count)