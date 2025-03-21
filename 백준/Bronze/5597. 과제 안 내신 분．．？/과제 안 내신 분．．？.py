import sys
input=sys.stdin.readline

arr=[0 for _ in range(31)]

for _ in range(28):
    arr[int(input())] = 1

for i in range(1,31):
    if not arr[i]:
        print(i)