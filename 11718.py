# 조건이 없을 때 except를 이용해서 빼기
while True:
    try:
        print(input())
    except EOFError:
        break