import sys

input = sys.stdin.readline

n = int(input())

def check_msg(n):
    check_msg = [2,0,2,3]
    check_idx = 0
    for c in str(n):
        if int(c) == check_msg[check_idx]:
            check_idx += 1
        if check_idx == 4:
            return 1
    return 0

if n < 2023: print(0)
else: 
    cnt = 0
    for i in range(2023,n+1):
        if check_msg(i): cnt += 1
    print(cnt)
