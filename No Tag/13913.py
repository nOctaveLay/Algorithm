from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int,input().split())
max_num = 10**5 + 1
parent = [n] * max_num

def bfs():
    distance = [0] * max_num
    nvq = deque()
    nvq.append(n)
    while nvq:
        here = nvq.popleft()
        if here == k:
            print(distance[k])
            break
        next_position = [here - 1, here + 1, here * 2]
        for there in next_position:
            if there >= 0 and there < max_num:
                if not distance[there] :
                    distance[there] = distance[here] + 1
                    parent[there] = here
                    nvq.append(there)

def print_deque():
    q = deque()
    here = k
    while here != n:
        q.append(here)
        here = parent[here]
    q.append(n)
    while q:
        print(q.pop(),end = ' ')


bfs()
print_deque()