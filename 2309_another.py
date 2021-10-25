result_list = []
for i in range(9):
    result_list.append(int(input()))
sum_s = sum(result_list)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_s - (result_list[i] + result_list[j]) == 100:
            one = result_list[i]
            two = result_list[j]
result_list.remove(one)
result_list.remove(two)
result_list.sort()
for i in result_list:
    print(i)