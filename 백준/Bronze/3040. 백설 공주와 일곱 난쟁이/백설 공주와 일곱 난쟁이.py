import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
sum_arr = sum(arr)

for i in range(9):
    for j in range(i):
        if sum_arr - arr[i] - arr[j] == 100:
            print(*arr[:j],sep='\n')
            print(*arr[j+1:i],sep='\n')
            print(*arr[i+1:],sep='\n',end='')
            exit()
