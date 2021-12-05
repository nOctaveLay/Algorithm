import sys
from collections import deque
input = sys.stdin.readline
A = input().rstrip('\n')
B = input().rstrip('\n')
arr = [ 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

answer = ''
mixture = list()
for a,b in zip(A,B):
    mixture.append(arr[ord(a) - ord('A')])
    mixture.append(arr[ord(b) - ord('A')])

while len(mixture) > 2:
    temp_list = list()
    for i in range(len(mixture)-1):
        temp_list.append((mixture[i] + mixture[i+1])%10)
    mixture = temp_list

for i in mixture:
    sys.stdout.write(str(i))