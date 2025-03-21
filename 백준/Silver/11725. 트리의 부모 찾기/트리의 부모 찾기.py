import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5+2)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
parent_list = [-1 for _ in range(n+1)]

def dfs(parent):
    for child in tree[parent]:
       if parent_list[child] == -1:
           parent_list[child] = parent
           dfs(child) 
dfs(1)
print(*parent_list[2:],sep='\n')