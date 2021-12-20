import sys
from collections import deque
input = sys.stdin.readline

num = input().rstrip("\n")
sum_num = 0

for _ in range(len(num)):
    sum_num += int(num)
    num = num[-1]+num[:-1]
print(sum_num)