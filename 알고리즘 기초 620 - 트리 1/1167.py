import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
v = int(input())

tree = [[] for _ in range(v+1)]

for _ in range(v-1):
    edge_information = list(map(int,input().split()))
    data = edge_information[0]
    child_data = edge_information[1]
    child_distance = edge_information[2]
    tree[data].append([child_data,child_distance])
    tree[child_data].append([data,child_distance])

max_distance = 0
max_index = 0

# 그 다음 탐색을 어떻게 시켜야하지
def dfs(start,tree,result):
    for i,distance in tree[start]:
        if result[i] == 0:
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
print(max(result2),end='')