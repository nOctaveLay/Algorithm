import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int,input().split())

# bfs
def bfs(a,b):
    q = deque()
    next_q = deque()
    q.append(a)
    oper_min_value = 0

    while q:
        current_value = q.popleft()
        if current_value  == b:
            return oper_min_value+1
        # x 2
        if current_value * 2 <= b:
            next_q.append(current_value * 2)
        
        # str(val) + 1 
        if int(str(current_value) + '1') <= b:
            next_q.append(int(str(current_value) + '1'))

        if not len(q):
            oper_min_value += 1
            q = next_q
            next_q = deque()
    return -1

print(bfs(a,b))
