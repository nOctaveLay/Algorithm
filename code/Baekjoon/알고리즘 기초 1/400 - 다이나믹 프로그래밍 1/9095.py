import sys
iter_num = int(sys.stdin.readline())

def solve(input_num):
  if input_num <= 0: return 0
  elif input_num == 1: return 1
  else: return solve(input_num-3) + solve(input_num-2) + solve(input_num-1) + (1 if input_num <= 3 else 0)

for _ in range(iter_num):
    n = int(sys.stdin.readline())
    print(solve(n))

#2747