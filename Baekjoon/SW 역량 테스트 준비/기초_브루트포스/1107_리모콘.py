import sys
n = int (sys.stdin.readline())
not_used_num = int(sys.stdin.readline())
if not_used_num != 0:
    not_used_list = set(sys.stdin.readline().rstrip("\n").split(" "))
else:
    not_used_list = set()
up_n, down_n = n,n
up_side, down_side = len(str(n)),len(str(n))

# 100에서 이동하는 경우
min_cnt = abs(100 - n)

# x 채널에서 이동하는 경우
for x in range(10**6):
    check = 0
    for y in str(x):
        # 만약에 사용할 수 없는 번호가 있다면, 나와라
        if y in not_used_list: 
            check = 1
            break
    if check == 0: 
        min_cnt = min(min_cnt, abs(x-n) + len(str(x)))

print(min_cnt)
