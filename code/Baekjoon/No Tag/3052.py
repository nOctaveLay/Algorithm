import sys
input = sys.stdin.readline
count = 0
r_list = list()
for _ in range(10):
    n = int(input())
    r = n % 42
    if not n % 42 in r_list:        
        r_list.append(n % 42)
        count += 1
sys.stdout.write(str(count))