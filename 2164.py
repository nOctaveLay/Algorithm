import queue
input_num = int(input())
q = queue.Queue()
[q.put(x) for x in range(1,input_num+1)]
while True:
	if q.qsize() == 1: break
	q.get()
	elem = q.get()
	q.put(elem)
print(q.get())