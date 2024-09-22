from collections import deque
def solution(priorities, location):
    priority_queue = sorted(priorities, reverse = True)
    process_ready_queue = deque()
    for index, priority in enumerate(priorities):
        process_ready_queue.append([index,priority])
    answer = 1
    while process_ready_queue:
        ready_process = process_ready_queue.popleft()
        # 만약 우선순위가 더 높은 프로세스가 없다면 프로세스 실행
        if ready_process[1] == priority_queue[answer - 1]:
            # 만약 이 놈이 location이라면 answer를 출력
            if ready_process[0] == location:
                return answer
            # 아니면 answer += 1
            answer += 1
        else:
            process_ready_queue.append(ready_process)
    return answer