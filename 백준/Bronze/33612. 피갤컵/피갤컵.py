import sys

input = sys.stdin.readline
n=int(input())

m = 8 + (7*(n-1))

print(2024 + (m//12) if m%12 !=0 else 2024+ m//12 - 1, (m % 12) if m%12 != 0 else 12)