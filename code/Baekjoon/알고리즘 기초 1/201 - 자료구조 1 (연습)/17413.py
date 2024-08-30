import sys
from collections import deque
input = sys.stdin.readline
input_list = input().rstrip("\n")

def print_deque(deq):
    for x in deq:
        sys.stdout.write(x)

count = 0
temp_string = deque()
for char in input_list:
    if char == '<':
        print_deque(temp_string)
        temp_string = deque()
        count = 1    
        sys.stdout.write(char)
    elif char == '>':
        count = 0
        sys.stdout.write(char)
    elif count == 1:
        sys.stdout.write(char)
    elif char == ' ':
        print_deque(temp_string)
        temp_string = deque()
        sys.stdout.write(char)
        
    else:
        temp_string.appendleft(char)
print_deque(temp_string)
temp_string = deque()
        

