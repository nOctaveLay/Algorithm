import sys
iter_num = int(sys.stdin.readline())
for _ in range(iter_num):
    a,b = sys.stdin.readline().split(" ")
    answer = int(a) + int(b)
    sys.stdout.write(f'{str(answer)}\n')