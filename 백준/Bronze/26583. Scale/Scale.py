import sys

input = sys.stdin.readline

while True:
    input_string = input().rstrip()
    if input_string == '': break
    num_list = list(map(int,input_string.split()))
    result_list = [1] * len(num_list)
    for i in range(len(num_list)):
        if i > 0:
            result_list[i] *= num_list[i-1]
        if i < len(num_list)-1:
            result_list[i] *= num_list[i+1]
        result_list[i] *= num_list[i]
    print(*result_list,sep=' ')