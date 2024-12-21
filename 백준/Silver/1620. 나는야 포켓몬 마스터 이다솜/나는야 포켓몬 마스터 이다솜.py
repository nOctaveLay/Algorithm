n,m=map(int,input().split())

str_to_int = dict()
int_to_str = dict()

for i in range(1,n+1):
    poketmon_name = input().rstrip()
    str_to_int[poketmon_name] = i
    int_to_str[i] = poketmon_name

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(int_to_str[int(q)])
    else:
        print(str_to_int[q])

