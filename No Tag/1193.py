input_num = int(input())
#1->1, 2->2, 3->2, 4->3 ...
count = 1
result = 1
while result <input_num:
	count += 1
	result += count
result = result - count
delta = input_num - result
if count %2 == 0:
	print(str(delta)+"/"+str(count+1-delta))
else:
	print(str(count+1-delta)+"/"+str(delta))
