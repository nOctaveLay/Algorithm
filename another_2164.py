import queue
n=int(input());q=queue.Queue();[q.put(x+1) for x in range(n)]
while q.qsize()>1:q.get();a=q.get();q.put(a)
print(q.get())