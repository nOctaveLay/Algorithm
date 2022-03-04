import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
1. 일단 회의가 빨리 끝나는 것을 찾아. -> 그 시간을 end에 저장함
2. 끝나자마자 시작하는 게 제일 빠르겠지? 끝나자마자 시작하는 것들 중에서 제일 빨리 끝나는 걸 찾아.
3. 끝나기 전에 시작하는 것은 list에서 세지 않아.
4. 마지막까지 search 했을 때 나온 cnt가 정답.
'''

def return_max_count_consult(time_list):
    time_list = sorted(time_list, key=lambda x: (x[1],x[0]))
    end = 0
    cnt = 0
    for i, j in time_list:
    #끝나는 것 중에서 빨리 시작하면, 이 i번째 수는 반드시 제일 빨리 끝나게 되어있다. (sort 우선순위가 x[1]이기 때문에)
    
        if i >= end: 
            cnt += 1
            end = j
    
    return cnt
    
if __name__ == "__main__":
    n = int(input())
    time_list = list()
    for _ in range(n):
        time_list.append(list(map(int,input().split())))
    output(str(return_max_count_consult(time_list)))