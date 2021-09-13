def times(x:int,y:int):
    distance = abs(y-x)
    k = int(distance ** (1/2))
    if distance - (k*k) == 0:
       return 2*k-1
    elif distance - (k*k) < k+1:
        return 2*k
    else:
        return 2*k+1
iter_num = int(input())
for _ in range(iter_num):
    input_list = input().split(" ")
    start,end = input_list
    start,end = int(start),int(end)
    print(times(start,end))
