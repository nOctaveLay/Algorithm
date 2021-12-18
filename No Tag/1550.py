import sys

input = sys.stdin.readline
a = input().rstrip("\n")
b = int('0x'+a,16)
print(b)