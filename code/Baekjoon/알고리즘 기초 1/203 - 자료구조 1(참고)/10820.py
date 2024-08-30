import sys
input = sys.stdin.readline
while True:
    input_string = input().rstrip("\n")
    if not input_string: break
    result = [0,0,0,0]
    for i in input_string:
        if i.islower():
            result[0] += 1
        elif i.isupper():
            result[1] += 1
        elif i.isnumeric():
            result[2] += 1
        elif i == ' ':
            result[3] += 1
    print(*result)