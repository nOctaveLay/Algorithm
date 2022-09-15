import sys
from collections import deque
a,b = map(int,input().split())
x = int(input())
num = list(map(int,input().split()))
base = 0
result = deque()

for i,elem in enumerate(reversed(num)):
    base += elem * a ** (i)
while base:
    result.appendleft(base % b)
    base //= b
print(*result)