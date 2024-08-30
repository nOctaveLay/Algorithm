import sys
input = sys.stdin.readline

def count_num_of_bar(expression):
    stack = []
    count = 0
    for i in range(len(expression)):
        #스택 쌓기
        if expression[i] == '(':
            stack.append('(')

        else:
            stack.pop()
            # 만약 레이저를 쏠 경우
            if expression[i-1] == '(': 
                count += len(stack)
            # bar만 확인했을 경우
            else:
                count += 1 
    return count

if __name__ == "__main__":
    print(count_num_of_bar(input().rstrip("\n")), end = '')