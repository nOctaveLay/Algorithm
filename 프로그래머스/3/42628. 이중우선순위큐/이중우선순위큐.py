import heapq

def solution(operations):
    answer = []
    heap = []
    # python의 heapq는 최소 힙이다.
    # 하지만 heapq는 list를 쓰기 때문에, list의 method - max, min 등을 쓸 수 있다. (공식 documentation에서도 권장
    # Step0: heap으로 만들어주기
    heapq.heapify(heap)
    # Step1: 명령어 분류
    for operation in operations:
        operation = operation.split(" ")
        # 삽입
        if operation[0] == 'I':
            heapq.heappush(heap,int(operation[1]))
        
        # 삭제
        elif operation[0] == 'D':
            # 빈 큐에 데이터를 삭제하라고 할 시 : 무시
            if len(heap) == 0: continue
            
            # 최댓값 삭제
            elif operation[1] == '1':
                heap.pop(heap.index(max(heap)))
        
            # 최솟값 삭제
            else: 
                heapq.heappop(heap)
        else: pass
    if len(heap) == 0: answer = [0,0]
    else: answer = [max(heap),min(heap)]
    
    return answer