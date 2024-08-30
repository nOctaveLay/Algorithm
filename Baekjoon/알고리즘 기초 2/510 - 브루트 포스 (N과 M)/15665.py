from itertools import product
n, m = map(int,input().split())
a = sorted(list(product(set(map(int,input().split())),repeat = m)))
for i in a:
    print(*i)