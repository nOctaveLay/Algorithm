from collections import deque
import sys
# sys.stdin.readlines는 어떻게 입력받는걸까?

iter_num = int(sys.stdin.readline())
deq = deque()

for _ in range(iter_num):
    operator = sys.stdin.readline().rstrip("\n").split(" ")
    if operator[0] == 'push_front':
        deq.appendleft(operator[1])
    elif operator[0] == 'push_back':
        deq.append(operator[1])
    elif operator[0] == 'pop_front':
        try: print(deq.popleft())
        except IndexError: print(-1)
    elif operator[0] == 'pop_back':
        try: print(deq.pop())
        except IndexError: print(-1)
    elif operator[0] == 'size':
        print(len(deq))
    elif operator[0] == 'empty':
        print(1 if len(deq) == 0 else 0)
    elif operator[0] == 'front':
        try: 
            a = deq.popleft()
            print(a)
            deq.appendleft(a)
        except IndexError: print(-1)
    elif operator[0] == 'back':        
        try: 
            a = deq.pop()
            print(a)
            deq.append(a)
        except IndexError: print(-1)
    else:
        print(-1)
