import sys
from itertools import combinations

input=sys.stdin.readline
# 0-9 까지의 숫자를 combinations으로 뽑은 것과 같음 
# (순서를 다르게 뽑아도 결국 내림차순)으로 정렬해야 되기 때문에 그렇다.
# 중복 허용 안됨 (예제에 322는 안된다고 설명)
n=int(input())
arr = []
if n > 1022 : print(-1) # sum(10Cr) r은 1-10 까지의 범위이므로. 1023개이나 0번째가 0임
else:
    for i in range(1,11):
        for j in combinations(range(10),i):
            arr.append(int(''.join(map(str,reversed(j)))))

    arr = sorted(arr)
    print(arr[n])
