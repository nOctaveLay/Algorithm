'''
component의 갯수는 dfs가 호출된 횟수를 찾아보면 된다.

n : 정점의 개수
m : 간선의 개수

dfs에서 그래프를 그렸을 시
인접 리스트의 실행 시간은 O(|n| + |m|)이고,
인접 행렬의 실행 시간은 O(|n|^2) 이므로, 
이 경우 인접 리스트로 그래프를 구현하는 것이 훨씬 낫다고 생각한다.

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int,input().split()) #n : 정점의 개수, m : 간선의 개수
visited = [0 for _ in range(n+1)]

# 1. 인접 리스트를 만든다.
adjacent = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())

    # 그래프의 방향성 x = 양쪽 다 관계가 있음
    adjacent[u].append(v)
    adjacent[v].append(u)

# dfs 구현

def dfs(i):
    for vertex in adjacent[i]:
        if not visited[vertex]:
            visited[vertex] = 1
            dfs(vertex)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count,end = '')