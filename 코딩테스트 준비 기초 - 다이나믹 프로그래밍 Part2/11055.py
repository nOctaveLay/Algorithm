import sys

input = sys.stdin.readline

n = int(input())
arr_list = list(map(int,input().split(" ")))
solve = arr_list[:]

for i in range(n):
    for j in range(i):
        if arr_list[i] > arr_list[j]:
            solve[i] = max(arr_list[i]+solve[j],solve[i])
print(max(solve), end= '')
