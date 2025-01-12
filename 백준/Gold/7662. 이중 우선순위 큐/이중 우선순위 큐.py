import sys
import heapq
input=sys.stdin.readline # overhead 제거
t=int(input())

for _ in range(t):
    k=int(input())
    # main data set
    '''
    if real_data[n] > 0 : 실제로 n이라는 데이터가 존재
        if real_data[n] = 1 : 데이터 하나만 존재
        else: 데이터가 중복해서 존재
    else: n이라는 데이터가 존재하지 않음
    
    # queue : O(logn)의 시간 복잡도를 가짐
    # queue 를 2개 쓴다면 O(logn) -> log(10**7) = 7
    # 최대값 / 최소값을 찾을 때 쓸 예정.
    # sort 하는 방식은 시간이 넘어감 7 * 10 ** 7
    '''
    real_data = dict()
    # heapq는 기본적으로 최소힙.
    # 최대힙을 구하려면 trick이 필요. (원 값에 -를 붙여 최소힙으로도 처리 가능한 형태로 만들고, 다시 -을 붙여 원 값으로 되돌림)
    max_heap = []
    min_heap = []
    # print(real_data, max_heap, min_heap) # debug 코드
    for _ in range(k):
        oper, n = input().rstrip().split()
        n = int(n)
        if oper == 'I':
            if n not in real_data: # 처음 삽입하는 경우
                real_data[n] = 1 # 데이터 하나만 존재한다 표기
                heapq.heappush(max_heap, -n)
                heapq.heappush(min_heap, n)
            else:# heapq 는 최대 / 최소를 빨리 뽑기 위한 공간이므로, 중복해서 값을 넣을 필요가 없다.
                real_data[n] += 1        
            # print(real_data, max_heap, min_heap) # debug 코드
        else: # oper == 'D':
            # 만약 Q가 비어있는데 적용할 연산이 D라면 무시해도 된다.
            # 즉 real_data에 값이 있을 때만 삭제해야 한다.
            if len(real_data) > 0:
                if n == 1: # 최대값을 삭제할 경우
                    max_value = -heapq.heappop(max_heap) #음수로 max_heap에 집어넣었으니, 실제 값은 -를 붙여서 빼줘야 한다.
                    # real_data에 max_value가 없다면 min_heap에서 제거 되어 real_data에 반영 되었지만, max_heap에는 반영되지 않은 데이터일 것이다.
                    # print(real_data,"max_value:",max_value,"max_heap:",max_heap, max_value in real_data) # debug 코드
                    while max_value not in real_data: 
                        max_value = -heapq.heappop(max_heap)
                        # print(real_data,"max_value:",max_value,"max_heap:",max_heap, max_value in real_data) # debug 코드
                    # print(real_data) # debug code
                    # real_data에 있는 값이 나왔을 것이다.
                    # 중복값도 계산 해줘야 댐
                    
                    real_data[max_value] -= 1
                    # print(real_data, real_data[max_value]) # debug code
                    if real_data[max_value] == 0:
                        del(real_data[max_value])
                    else:
                        heapq.heappush(max_heap,-max_value)
                    # print(real_data) # debug code

                else: # 최소값을 삭제할 경우
                    min_value = heapq.heappop(min_heap) 

                    # real_data에 min_value가 없다면 max_heap에서 제거 되어 real_data에 반영 되었지만, min_heap에는 반영되지 않은 데이터일 것이다.
                    # print(real_data,"min_value:",min_value,"min_heap:",min_heap, min_value in real_data) # debug 코드
                    while min_value not in real_data: 
                        min_value = heapq.heappop(min_heap) 
                        # print(real_data,"min_value:",min_value,"min_heap:",min_heap, min_value in real_data) # debug 코드
                    # print(real_data) # debug code
                    # real_data에 있는 값이 나왔 것이다.
                    real_data[min_value] -= 1
                    if real_data[min_value] == 0:
                        del(real_data[min_value])
                    else:
                        heapq.heappush(min_heap,min_value)
                    # print(real_data) # debug code
                # print(real_data,"max_heap",max_heap, "min_heap",min_heap) # debug code

    if len(real_data) == 0:
        print('EMPTY')
    else:
        min_value = heapq.heappop(min_heap)
        while min_value not in real_data and len(min_heap) > 0:
            min_value = heapq.heappop(min_heap)
        max_value = -heapq.heappop(max_heap)
        while max_value not in real_data and len(max_heap) > 0:
            max_value = -heapq.heappop(max_heap)
        
        # while min_heap[0] not in real_data or real_data[min_heap[0]] < 1:
        #     heapq.heappop(min_heap)
        # while -max_heap[0] not in real_data or real_data[-max_heap[0]] < 1:
        #     heapq.heappop(max_heap)
        print(max_value, min_value)


