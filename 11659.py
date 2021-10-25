import sys
n,m = map(int,sys.stdin.readline().rstrip("/n").split(" "))
n_number = sys.stdin.readline().rstrip("/n").split(" ")
sum_list = list()
sum_list.append(int(n_number[0]))

for i in range(1,n):
    sum_list.append(sum_list[i-1] + int(n_number[i]))
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip("/n").split(" "))
    if a > 1:
        print(sum_list[b-1]-sum_list[a-2])
    else:
        print(sum_list[b-1])