import queue
inputlist = input().split(" ")
input_num,k = int(inputlist[0]), int(inputlist[1])
q = queue.Queue()
[q.put(x) for x in range(1,input_num+1)]
a = 1
result_list = []
while True:
	if q.qsize() == 0: break
	elem = q.get()
	if a == k:
		a = 1
		result_list.append(elem)
	else:
		q.put(elem)
		a += 1
print("<",end='')
for x in result_list:
	if x != result_list[-1]:
		print(x,end=', ')
	else: print(x,end="")
print(">",end='')