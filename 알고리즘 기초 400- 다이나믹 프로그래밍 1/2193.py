import sys

input = sys.stdin.readline

n = int(input())
result0,result1 = 1,1

for _ in range(1,n):

    temp0 = result0 + result1
    temp1 = result0

    result0 = temp0
    result1 = temp1
    
print(result1)