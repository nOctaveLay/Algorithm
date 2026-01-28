import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    print("Class",i+1)

    arr = sorted(arr[1:],reverse=True)
    lg = 0
    for i in range(len(arr)-1):
        gap = arr[i] - arr[i+1]
        lg = max(lg, gap)
    
    print(f"Max {arr[0]}, Min {arr[-1]}, Largest gap {lg}")
