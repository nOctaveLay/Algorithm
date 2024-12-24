import sys
input=sys.stdin.readline
n_computer=int(input())
n_connect=int(input())
computer_relationship=dict()
def insert_values(a,b):
    if a not in computer_relationship:
        computer_relationship[a] = [b]
    else:
        computer_relationship[a].append(b)
#ready for data
for _ in range(n_connect):
    a,b=map(int,input().split())
    insert_values(a,b)
    insert_values(b,a)
visited=[False for _ in range(n_computer+1)]
def dfs(current_node):
    visited[current_node] = True # 방문함
    if current_node not in computer_relationship: return 0
    for next_node in computer_relationship[current_node]:
        if not visited[next_node]: # 방문하지 않았을 경우
            dfs(next_node) #방문함
dfs(1)
print(sum(visited)-1)