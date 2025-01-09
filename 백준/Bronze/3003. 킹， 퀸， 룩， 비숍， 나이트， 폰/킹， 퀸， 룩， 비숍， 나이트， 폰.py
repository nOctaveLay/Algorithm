import sys
input=sys.stdin.readline
arr=list(map(int,input().split()))
correct_arr = [1,1,2,2,2,8]

for i,j in zip(arr,correct_arr):
    print(j-i,end=' ')
