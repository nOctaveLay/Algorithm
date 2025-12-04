import sys
input=sys.stdin.readline

MAXLENGTH = 1000001
arr = ["EMPTY"] * MAXLENGTH

for i in range(1,MAXLENGTH,2):
    arr[i] = 'O'

for i in range(1001):
    square_i = i*i
    if square_i % 2 == 0:
        arr[square_i] = 'S'
    else:
        arr[square_i] = 'OS'


for _ in range(int(input())):
    print(arr[int(input())])