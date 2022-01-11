import math
import sys
input = sys.stdin.readline
n = int(input())
num_sqrt_list = [i for i in range(n+1)]
max_num = int(n ** (1/2))
for i in range(n+1):
    j = int(math.sqrt(i+1))
    while j > -1:
        num_sqrt_list[i] = min(num_sqrt_list[i],1+num_sqrt_list[i- j*j])
        j -= 1
print(num_sqrt_list[n],end='')