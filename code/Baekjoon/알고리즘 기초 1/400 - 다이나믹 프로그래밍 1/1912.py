import sys
input = sys.stdin.readline
n = int(input())
seq =  list(map(int,input().split()))
max_sum_value = [i for i in seq]

for i in range(1,n):
    max_sum_value[i] = max(max_sum_value[i],max_sum_value[i-1] + max_sum_value[i])

print(max(max_sum_value), end='')