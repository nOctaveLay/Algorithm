import sys
iter_num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

min_val = min(arr)
max_val = max(arr)

print(min_val,max_val,end='')