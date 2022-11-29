import sys
input = sys.stdin.readline
v = int(input())

# node_count == 0 : 루트로 삼아도 문제 없다.

node_count = [-1 for _ in range(v+1)] 
tree = [[] for _ in range(v+1)]
result = [0 for _ in range(v+1)]

for _ in range(v):
    edge_information = list(map(int,input().split()))
    edge_information = edge_information[:-1]
    data = edge_information[0]
    node_count[data] += 1
    for i in range(1,len(edge_information),2):
        child_data = edge_information[i]
        child_distance = edge_information[i+1]
        tree[data].append([child_data,child_distance])
        node_count[child_data] += 1

max_distance = 0
max_index = 0

# 그 다음 탐색을 어떻게 시켜야하지
def dfs(start,tree,result):
    for i,distance in tree[start]:
        if result[i] == 0:
            result[i] = 1
            result[i] = result[start] + distance
            dfs(i,tree,result)

result1 = [0 for _ in range(v+1)]
result2 = [0 for _ in range(v+1)]

dfs(1,tree,result1)
result1[1] = 0
for i,distance in enumerate(result1):
    if max_distance < distance :
        max_distance = distance
        max_index = i
dfs(max_index,tree,result2)
result2[max_index] = 0
print(max(result2))