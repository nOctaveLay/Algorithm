from collections import deque
import sys

def bfs(state_a,state_b,state_c):
    q = deque()
    num_of_visited[(state_a,state_b,state_c)] = 0
    q.append((state_a,state_b,state_c,0))

    while q:
        a,b,c,cnt = q.popleft()

        if a:
            top = a[-1]
            l = a[:-1]
            try: num_of_visited[(l ,b + top, c)]
            except: 
                num_of_visited[(l, b + top, c)] = cnt + 1
                q.append((l, b + top, c, cnt+1))

            try: num_of_visited[(l, b, c + top)]
            except:
                num_of_visited[(l, b, c + top)] = cnt + 1
                q.append((l, b, c + top, cnt+1))
                
        if b:
            top = b[-1]
            l = b[:-1]
            try: num_of_visited[(a + top, l, c)]
            except:
                num_of_visited[(a + top, l, c)] = cnt + 1
                q.append((a + top, l, c, cnt+1))

            try: num_of_visited[(a, l, c + top)]
            except:
                num_of_visited[(a, l, c + top)] = cnt + 1
                q.append((a, l, c + top, cnt+1))
                
        if c:
            top = c[-1]
            l = c[:-1]
            try: num_of_visited[(a + top, b, l)]
            except:
                num_of_visited[(a + top, b, l)] = cnt + 1
                q.append((a + top, b, l, cnt+1))
            try: num_of_visited[(a, b + top, l)]
            except:
                num_of_visited[(a, b + top, l)] = cnt + 1
                q.append((a, b + top, l, cnt+1))


if __name__ == "__main__":
    input = sys.stdin.readline
    num_of_a, num_of_b, num_of_c = 0,0,0
    state = list()
    for i in range(3):
        line = input().rstrip()
        state.append('' if len(line) == 1 else line.split()[1])
        num_of_a += state[i].count('A')
        num_of_b += state[i].count('B')
        num_of_c += state[i].count('C')
        
    num_of_visited = dict()
    bfs(*state)
    last = ('A'*num_of_a,'B'*num_of_b,'C'*num_of_c)
    print(num_of_visited[last])