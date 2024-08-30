import sys
def print_star(n):
    for i in range(n):
        if i % 2 == 0:
            for _ in range(n-1):
                print('*',end = ' ')
            print('*')
        else:
            for _ in range(n-1):
                print(' *',end = '')
            print(' *')
print_star(int(sys.stdin.readline()))