import sys

input = sys.stdin.readline


h_price = min([int(input()) for _ in range(3)])
d_price = min([int(input()) for _ in range(2)])

print(h_price+d_price-50)