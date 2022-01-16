import sys

input = sys.stdin.readline
n = int(input())
tree_list = [list(map(int,input().split(" "))) for _ in range(n)]
sum_tree_list = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(len(tree_list[i])-1):
        sum_tree_list[i][j] = tree_list[i][j] + max(sum_tree_list[i-1][j-1], sum_tree_list[i-1][j])    
    j = len(tree_list[i])-1
    sum_tree_list[i][j] = tree_list[i][j] + sum_tree_list[i-1][j-1]

print(max(sum_tree_list[n-1]), end= '')