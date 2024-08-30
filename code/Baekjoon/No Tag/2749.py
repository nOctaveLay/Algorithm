import sys
from collections import deque
input_num = int(sys.stdin.readline())

# 나는 피사노 주기를 이용할 것이다.
m = 1 * 10 ** 6
k = 15 * 10 ** 5
fibo_list = [0 for x in range(k)]
fibo_list[1] = 1 #초기 조건

for fibo_index in range(2,len(fibo_list)):
	fibo_list[fibo_index] = (fibo_list[fibo_index-1] + fibo_list[fibo_index-2]) % m


sys.stdout.write(str(fibo_list[input_num % k]))
