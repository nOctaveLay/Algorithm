import sys

input=sys.stdin.readline

input_string = input().rstrip()

while input_string != "#":
    count = 0
    for c in input_string:
        if c.lower() in ['a','e','i','o','u']:
            count += 1
    print(count)
    
    input_string = input().rstrip()