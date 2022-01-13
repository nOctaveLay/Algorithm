import sys
from unittest import case
input = sys.stdin.readline

n = int(input())
case_list = [[0]*3 for _ in range(n)]

# 초기조건
case_list[0] = [1,1,1]

for i in range(1,n):
    case_list[i][0] = (case_list[i-1][0] + case_list[i-1][1] + case_list[i-1][2]) % 9901
    case_list[i][1] = (case_list[i-1][0] + case_list[i-1][2]) % 9901
    case_list[i][2] = (case_list[i-1][0] + case_list[i-1][1]) % 9901

print(sum(case_list[n-1]) % 9901)