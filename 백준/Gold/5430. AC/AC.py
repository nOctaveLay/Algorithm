from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    p=list(map(str,input().rstrip()))
    n=int(input())
    # 굳이 뒤집기를 해야할까?
    arr_string = input().rstrip()
    arr=deque(map(int,arr_string[1:-1].split(","))) if arr_string != '[]' else deque()
    head=0
    error=0
    for command in p:
        if command == 'R':
            if head == 0:
                head = -1
            else:
                head = 0
        else:
            if len(arr) == 0: 
                print("error")
                error = 1
                break
            else:
                if head == 0: arr.popleft()
                else: arr.pop()
    if not error:
        if head == -1:
            print("[",end='')
            for i in range(len(arr)-1,0,-1):
                print(arr[i],end=',')
            if len(arr) > 0: print(arr[0],end='')
            print("]",sep='',end='\n')
        else:
            print("[",end='')
            print(*arr,sep=',',end=']')
            print()