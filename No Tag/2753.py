import sys
input = sys.stdin.readline
a = int(input())

def isyun(a):
    if a % 4 == 0:
        if a % 100 != 0 or a % 400 == 0:
            return 1
    return 0

print(isyun(a))