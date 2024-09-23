from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weights = 0
    current = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    while current:
        answer +=1
        # 다리를 지난 트럭으로 이동
        now = current.popleft()
        total_weights -= now
        
        # 대기 트럭이 남아있다면, 다리에 일단 넣어보고 무게보다 크면 안넣고, 무게보다 작으면 넣는다.
        if truck_weights:
            if total_weights+truck_weights[0] <= weight:
                current.append(truck_weights.popleft())
                total_weights += current[-1]
            else: 
                current.append(0)
    return answer