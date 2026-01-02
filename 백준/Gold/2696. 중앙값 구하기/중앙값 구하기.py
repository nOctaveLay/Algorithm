import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    arr_max_value = n//10 if n % 10 == 0 else n//10+1
    for _ in range(arr_max_value):
        arr += list(map(int, input().split()))
    left_queue = [] # 최대 힙으로 만들 예정, 중간 값보다 작은 수만 들어감
    right_queue = [] # 최소 힙, 중간 값보다 큰 수만 들어감

    answer = []
    for i in arr:
        # left_queue와 right_queue가 서로 같을 때 -> left_queue부터 넣기
        if len(left_queue) == len(right_queue):
            heapq.heappush(left_queue,-i)
        else:
            heapq.heappush(right_queue,i)

        # 균등화
        if right_queue and -left_queue[0] > right_queue[0]:
            # 추출
            min_value = heapq.heappop(right_queue)
            max_value = heapq.heappop(left_queue)

            # 삽입
            heapq.heappush(left_queue,-min_value)
            heapq.heappush(right_queue,-max_value)
        # 홀수 일 때만 출력
        if len(left_queue) != len(right_queue):
            answer.append(-left_queue[0])
    
    print(len(answer))
    for i in range(0,len(answer),10):
        print(*answer[i:i+10])
