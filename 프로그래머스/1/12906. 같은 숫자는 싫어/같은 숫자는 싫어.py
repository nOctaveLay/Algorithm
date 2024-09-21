def solution(arr):
    answer = []
    for arr_i in arr:
        if len(answer) == 0:
            answer.append(arr_i)
        elif answer[-1] != arr_i:
            answer.append(arr_i)
    return answer