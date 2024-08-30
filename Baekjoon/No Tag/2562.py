import sys

max_num = 0
max_index = 1
for i in range(1,10):
    iter_num = int(sys.stdin.readline())
    if max_num < iter_num:
        max_num = iter_num
        max_index = i

sys.stdout.write(str(max_num)+"\n")
sys.stdout.write(str(max_index))