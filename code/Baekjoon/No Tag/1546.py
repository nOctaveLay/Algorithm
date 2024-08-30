#1546 average.py
in_num = int(input())
string = input().split()
temp_list = []
for x in range(len(string)):
	temp_list.append(int(string[x]))
string = temp_list
max_n = max(string)
sum_n = 0
for x in string:
	sum_n += x/max_n*100 #round is error
aver = sum_n/in_num #round is error
print("%0.2f"%aver)