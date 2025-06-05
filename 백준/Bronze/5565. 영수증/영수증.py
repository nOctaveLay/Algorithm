import sys
input=sys.stdin.readline

product_sum = int(input())
product_prices = [int(input()) for _ in range(9)]

print(product_sum - sum(product_prices))
