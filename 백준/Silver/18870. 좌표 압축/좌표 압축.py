import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
value_to_index = {value:index for index,value in enumerate(sorted(list(set(arr))))}
print(*list(value_to_index[i] for i in arr))
