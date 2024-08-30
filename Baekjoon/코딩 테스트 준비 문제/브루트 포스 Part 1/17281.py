import sys
input = sys.stdin.readline
from itertools import permutations

def make_members(permutate:tuple):
    members = [0 for _ in range(9)]
    for i in range(3):
        members[i] = permutate[i]
    members[3] = 0
    for i in range(3,8):
        members[i+1] = permutate[i]
    return members

def play_game():
    max_score = 0
    # 사람의 타순을 정합니다.
    for permutate in permutations(range(1,9)):
        members = make_members(permutate)
        next_member_idx = 0 # 다음 타자의 idx를 추적합니다.
        score = 0 # 총 스코어

        for ining_lists in arr:
            out_count = 0
            f1, f2, f3 = 0, 0, 0

            while out_count < 3:  # out_count가 3이 넘어가면, 그 즉시 이닝 종료.
                next_member = members[next_member_idx]
                member_state = ining_lists[next_member]

                # 선수의 state에 따라 행동을 달리한다.
                if member_state == 0: # 아웃 당했을 경우
                    out_count += 1

                elif member_state == 1:
                    score += f3
                    f1, f2, f3 = 1, f1, f2

                elif member_state == 2:
                    score += (f2 + f3)
                    f1, f2, f3 = 0, 1, f1

                elif member_state == 3:
                    score += (f1 + f2 + f3)
                    f1, f2, f3 = 0, 0, 1

                elif member_state == 4: # 홈런일 경우
                    score += (f1 + f2 + f3 + 1)
                    f1, f2, f3 = 0, 0, 0

                next_member_idx = (next_member_idx + 1) % 9
        max_score = max(max_score, score)
    return max_score

if __name__ == "__main__":
    # 초기 조건
    n = int(input()) # 이닝수 
    arr = list(list(map(int,input().split())) for _ in range(n)) # 이닝수 리스트
    print(play_game())
    