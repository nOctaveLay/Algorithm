import sys
from collections import deque

input = sys.stdin.readline

front_stack = deque(input().rstrip('\n'))

end_stack = deque()
iter_num = int(input())

for _ in range(iter_num):
    set_of_operator = input().rstrip('\n').split(" ")
    operator = set_of_operator[0]
    
    if operator == 'L':
        if len(front_stack) != 0:
            temp_char = front_stack.pop() # 오른쪽 반환
            end_stack.appendleft(temp_char)

    elif operator == 'D':
        if len(end_stack) != 0:
            temp_char = end_stack.popleft()
            front_stack.append(temp_char)

    elif operator == 'B':
        if len(front_stack) != 0:
            front_stack.pop()

    elif operator == 'P':
        add_char = set_of_operator[1]
        front_stack.append(add_char)
    

for x in front_stack:
    sys.stdout.write(x)
for y in end_stack:
    sys.stdout.write(y)