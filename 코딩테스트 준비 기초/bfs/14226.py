'''
1. 이건 3가지 연산을 한다.
2. 일단 클립보드에 이모티콘이 있는지 없는지 확인을 해야 되지 않나...?
3. queue에 누가 data를 하나만 저장할 수 있다고 알려줬지?
'''

from collections import deque
import sys
input = sys.stdin.readline

s = int(input()) # 목표로 하는 이모티콘의 개수
max_num = s+1 

'''
taken_time[screen][clipboard] : 화면에 이모티콘이 screen 만큼 남아있고, 클립보드에 이모티콘이 clipboard 만큼 남아있을 때 걸리는 시간.
nvq : not_visited_queue : 아직 방문하지 않은 곳 (곧 방문할 노드)를 추적하는 queue
'''

taken_time = [[0 for _ in range(max_num)] for _ in range(max_num)]
nvq = deque()
nvq.append([1,0])

while nvq:
    screen,clipboard = nvq.popleft()

    next_list = [[screen, screen], 
                [screen + clipboard, clipboard],
                [screen - 1, clipboard]]

    for next_screen, next_clipboard in next_list:        
        if next_screen >= 0 and next_screen < max_num:
            if taken_time[next_screen][next_clipboard] == 0:
                taken_time[next_screen][next_clipboard] = taken_time[screen][clipboard] + 1
                nvq.append([next_screen, next_clipboard])
min_num = max_num
for i in range(max_num):
    if taken_time[s][i] != 0:
        if taken_time[s][i] < min_num:
            min_num = taken_time[s][i]

print(min_num,end = '')
