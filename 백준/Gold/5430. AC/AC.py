from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    p=list(map(str,input().rstrip()))
    n=int(input())
    # 굳이 뒤집기를 해야할까?
    arr=deque(map(str,input().rstrip().strip('[]').split(','))) # [1,2,3,4] 를 list로 파싱하는 방법 

    # 만약 D의 개수가 n보다 많다면 -> 뺄 수 없으니까 error를 뱉음
    if n < p.count('D'):
        print("error")
    else:
        inverse = 0
        for command in p:
            if command == 'R':
                inverse = not inverse # inverse = 0 if inverse == 1 else 1
            else: # command == 'D'
                if not inverse: arr.popleft()
                else: arr.pop()
        if inverse:
            arr=reversed(arr)
        print(f"[{','.join(arr)}]")
