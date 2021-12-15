from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int,input().split())
result_list = list()
def print_iterator(iterator):
    print("<",end='')
    for elem in iterator[:-1]:
        print(f'{elem}, ',end='')
    print(f'{iterator[-1]}>',end = '')

yosep_queue = deque()
for i in range(1,n+1): yosep_queue.append(i) #오른쪽 끝에 삽입
while len(yosep_queue) != 0:
    for _ in range(k-1):
        yosep_queue.rotate(-1)
    a = yosep_queue.popleft()
    result_list.append(a)
print_iterator(result_list)