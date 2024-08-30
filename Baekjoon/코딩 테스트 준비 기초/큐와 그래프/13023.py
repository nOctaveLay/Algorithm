'''
1. 이 문제를 봤을 때 그래프 구조로 짜야 한다고 생각했다. (왜냐면 계층으로 이루어져 있지 않기 때문)
2. dfs를 해서, height인지를 검색하기만 하면 끝 아닌가?
'''
import sys

def dfs(start,tree):
    visited[start] = 1
    cnt = 0
    for i in tree[start]:
        if visited[i] == 0:
            visited[i] = 1
            cnt = max(cnt,dfs(i,tree)+1)
            if cnt > 3:
                return cnt
            visited[i] = 0
    return cnt

input = sys.stdin.readline
n,m = map(int,input().split())
tree = {i:[] for i in range(0,n)}
sys.setrecursionlimit(10**6)

for _ in range(m):
    v1, v2 = map(int,input().split())
    # 관계가 있음을 표현한다.
    tree[v1].append(v2)
    tree[v2].append(v1)

height = 0
for i in range(n):
    visited = [0 for _ in range(n)]
    height = max(height,dfs(i,tree))
    if height > 3:
        print(1,end='')
        exit()
print(0,end='')