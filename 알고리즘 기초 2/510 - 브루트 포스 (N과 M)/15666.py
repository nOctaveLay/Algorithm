from itertools import product
n, m = map(int,input().split())
a = sorted(list(product(set(map(int,input().split())),repeat = m)))
for i in a:
    flag = 1
    for j in range(len(i)-1):
        if i[j] > i[j+1]: 
            flag = 0
            break
    if flag: print(*i)