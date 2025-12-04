import sys
import math
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    a = int(input())
    if a % 2 == 1:
        print('O',end='')
    if (math.sqrt(a)).is_integer():
        print('S',end='')
    
    if a%2 ==0 and not (math.sqrt(a)).is_integer():
        print("EMPTY")
    else:
        print()