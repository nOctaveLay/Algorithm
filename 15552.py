import sys
iter_num = sys.stdin.readline().rstrip("/n")
for _ in range(int(iter_num)):
    input_num = sys.stdin.readline().rstrip("/n")
    a,b = map(int,input_num.split(" "))
    print(a+b)