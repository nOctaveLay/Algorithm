import sys
input=sys.stdin.readline

x = int(input())
k = 1
count = 0
while k < x+1:
    if x & k: count += 1
    k <<= 1
print(count)