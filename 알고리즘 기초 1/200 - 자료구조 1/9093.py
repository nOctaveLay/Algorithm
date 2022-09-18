import sys
input = sys.stdin.readline
iter_num = int(input())
for _ in range(iter_num):
    input_list = input().split()
    for i in input_list:
        for j in reversed(range(1,len(i))):
            print(i[j],end='')
        print(i[0],end = ' ')
    print()