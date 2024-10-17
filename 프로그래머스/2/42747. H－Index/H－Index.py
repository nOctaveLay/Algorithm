def solution(citations):
    answer = 0
    citations = sorted(citations)
    n = len(citations)
    for i in range(n):
        hIndex = n-i
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer