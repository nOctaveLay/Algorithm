import sys
input=sys.stdin.readline

n = int(input())
for _ in range(n):
    answer = 0 
    arr = list(map(int,input().split()))
    test_case, arr = arr[0], arr[1:]
    for i in range(1,len(arr)):
        for k in range(i):
            if arr[k] > arr[i]:
                temp = arr[i]
                for j in range(i,k,-1):
                    arr[j] = arr[j-1]
                answer += (i-k)
                arr[k] = temp
    print(test_case,answer)