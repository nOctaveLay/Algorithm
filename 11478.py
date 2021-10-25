input_string = input()
result_list = list()
for i in range(len(input_string)):
    for j in range(i+1,len(input_string)+1):
        result_list.append(input_string[i:j])
print(len(set(result_list)))
