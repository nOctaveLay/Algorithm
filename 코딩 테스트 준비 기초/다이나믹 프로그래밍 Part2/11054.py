import sys
from threading import local

input = sys.stdin.readline

n = int(input())
arr_list = list(map(int,input().split(" ")))
solve_asc = [1]* n
solve_desc = [1] * n

for i in range(n):
    for j in range(i):
        if arr_list[i] > arr_list[j]:
            solve_asc[i] = max(1+solve_asc[j], solve_asc[i])

for i in reversed(range(n)):
    for j in reversed(range(i,n)):
        if arr_list[i] > arr_list[j]:
            solve_desc[i] = max(1+solve_desc[j], solve_desc[i])

max_value = 0
for i in range(n):
    local_value = solve_asc[i] + solve_desc[i]-1
    if local_value > max_value:
        max_value = local_value

print(max_value,end = '')