import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_queue = [] # 중간값 x보다 작은 수들이 들어갈 곳. 최대힙
right_queue = [] # 중간값 x보다 큰 수들이 들어갈 곳. 최소힙
answer = []


for i in range(n):
    input_num = int(input())
    # 중간값은 모두 left_queue에서 관리한다.
    if len(left_queue) == len(right_queue):
        heapq.heappush(left_queue,-input_num) # 기본적으로 python의 heapq는 min_queue이므로, element를 저장할 때 부호를 바꿔서 저장하면 쉽게 max_queue로 만들 수 있다.
    else:
        # 항상 삽입 우선순위가 left_queue이므로, 둘의 개수가 같지 않다면 right_queue에서 부족할 것이다.
        heapq.heappush(right_queue,input_num)
    
    # left_queue에는 중간값보다 작은수가, right_queue에는 중간값보다 큰 수가 들어가야만 한다.
    # 하지만 삽입되는 놈이 중간값보다 작음에도 right_queue로 들어갈 수 있다.
    # 하지만 삽입되는 놈이 중간값보다 큼에도 left_queue로 들어갈 수 있다.
    # 따라서 left_queue의 큰 값과 right_queue의 작은 값을 비교해 중간값인지를 확인하고, 아닐 경우 서로 바꿔준다.
    if right_queue and -left_queue[0] > right_queue[0]:
        # 추출
        min_value = heapq.heappop(right_queue) 
        max_value = heapq.heappop(left_queue) # left queue는 음수로 저장된다.

        # 삽입
        heapq.heappush(left_queue, -min_value) # left queue는 음수로 저장된다.
        heapq.heappush(right_queue, -max_value)
    answer.append(-left_queue[0])

print(*answer,sep='\n')
    
