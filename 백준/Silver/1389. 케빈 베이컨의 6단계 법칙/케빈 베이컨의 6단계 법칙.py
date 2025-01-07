import sys
input=sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
friends = dict()
def add_relationship(data:dict, key:int, item:int):
    if key not in data:
        data[key] = set()
        data[key].add(item)
    else:
        data[key].add(item)
    return data

def bfs(v,visited):
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        current_v = q.popleft()
        for next_v in friends[current_v]:
            if not visited[next_v]:
                visited[next_v] = visited[current_v] + 1
                q.append(next_v)
    return visited

# make graph
for _ in range(m):
    a, b = map(int,input().split())
    friends = add_relationship(friends,a,b)
    friends = add_relationship(friends,b,a)

answer = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited = bfs(i,visited)
    answer.append(sum(visited))
print(answer.index(min(answer))+1)