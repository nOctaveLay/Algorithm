import sys
input=sys.stdin.readline
n,m=map(int,input().split())

str_to_int = dict()
for i in range(1,n+1):
    poketmon_name = input().rstrip()
    str_to_int[poketmon_name] = i

# 항상 일일히 할당하는 것보다 comprehension 이 더 빠르다.
int_to_str = {v:k for k, v in str_to_int.items()}

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(int_to_str[int(q)])
    else:
        print(str_to_int[q])

