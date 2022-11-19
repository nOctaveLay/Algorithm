import sys

n = int(sys.stdin.readline())
MODULER = 10007
asc_num_list = [[0] * 10 for _ in range(n)]

asc_num_list[0] = [1] * 10

for i in range(1,n):
    for j in range(10):
        asc_num_list[i][j] = sum(asc_num_list[i-1][j:]) % MODULER
print(sum(asc_num_list[n-1]) % MODULER,end='')
