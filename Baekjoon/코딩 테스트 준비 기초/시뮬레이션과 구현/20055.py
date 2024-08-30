from collections import deque
import sys

input = sys.stdin.readline

def move_robot(arr,k):
    robot_position = deque(0 for _ in range(n))
    answer = 0

    while True:
        answer += 1
        # rotate
        arr.rotate(1)
        robot_position.rotate(1)

        # 로봇 내리기
        robot_position[-1] = 0

        # move robot - need revised
        for i in reversed(range(1,n)): #n-1 ~ 0까지
            if robot_position[i-1] and arr[i] and not robot_position[i]:
                robot_position[i],robot_position[i-1] = robot_position[i-1],0
                arr[i] -= 1

        # 로봇 올리기
        if arr[0] > 0:
            robot_position[0] = 1
            arr[0] -= 1
        count = 0

        # 로봇 내리기
        robot_position[-1] = 0

        for elem in arr:
            if elem == 0:
                count += 1
        if count >= k:
            break
    return answer
        
if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = deque(map(int,input().split()))
    print(move_robot(arr,k))