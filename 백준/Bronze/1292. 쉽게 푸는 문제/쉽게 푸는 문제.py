import sys

input=sys.stdin.readline

a,b = map(int,input().split())

arr = list()
for i in range(1,b+1):
    for j in range(i):
        arr.append(i)

result = sum(arr[a-1:b])
print(result)