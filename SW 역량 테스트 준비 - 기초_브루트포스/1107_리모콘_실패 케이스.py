import sys

# 예외 케이스를 잘 생각하자.

n = int (sys.stdin.readline())
not_used_num = int(sys.stdin.readline())
if not_used_num != 0:
    not_used_list = sys.stdin.readline().rstrip("\n").split(" ")
else:
    not_used_list = list()
up_n, down_n = n,n
up_side, down_side = len(str(n)),len(str(n))

while True:
    down_check = 0
    for down_letter in str(down_n):
        if down_letter in not_used_list:
            down_n -= 1
            down_side += 1
            down_check = 1
            break
    if down_check == 0: break
    if down_n < 0 : break

while True:
    up_check = 0
    for up_letter in str(up_n):
        if up_letter in not_used_list:
            up_n += 1
            up_side += 1
            up_check = 1
            break
    if up_check == 0: break
    if up_n > 10 ** 6 : break

final_min = min(down_side,up_side,abs(100-n))
print(final_min)
