import sys
iter_num = int(sys.stdin.readline())
problem_list = [int(sys.stdin.readline()) for _ in range(iter_num)]
problem_list = sorted(problem_list)
for x in problem_list:
    sys.stdout.write(str(x)+"\n")