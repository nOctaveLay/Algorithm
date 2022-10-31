import sys
input = sys.stdin.readline
n = int(input())

axis = [0,0,0,0,0]
for _ in range(n):
    a, b = map(int,input().split())
    if a == 0 or b == 0: axis[-1] += 1
    elif a > 0:
        if b > 0:
            axis[0] += 1
        else:
            axis[3] += 1
    else:            
        if b > 0:
            axis[1] += 1
        else:
            axis[2] += 1
for i in range(4):
    print(f'Q{i+1}: {axis[i]}')
print(f'AXIS: {axis[-1]}')