import sys

L,U = sys.stdin.readline().rstrip("\n").split(" ")
L,U = int(L),int(U)
digit_num = list()
return_num = 0
k = 1

while True:

    if L > U: break

    # 만약 시작 자리가 0이 아니라면 0으로 만들어주는 과정을 거쳐야 한다.
    
    while True:
        if L % 10 != 0 and L < U:
            for i in str(L):
                return_num += int(i) * k
            L += 1


        # 끝 자리가 9가 아니라면 9로 만들어주는 과정을 거쳐야한다.
        # 만약 1-9일 경우, 0의 자리는 빼줘야 한다.
        
        elif U % 10 != 9 and U > L:
            # 예를 들어 40라는 수가 있으면 return_list[4] += 1, return_list[0] += 1
            for i in str(U):
                return_num += int(i) * k
            U -= 1
        
        elif L == U:
            for i in str(U):
                return_num += int(i) * k
            print(return_num)
            exit()
        else:
            break

    # n이 2자리 수가 넘을 경우
    if U > 9:
        # n이 k자리수라고 가정했을 때, (단 k >= 2)
        # k-1 자리수[즉, 1.. ~ n/10] 의 0-9까지의 갯수는 (10/10 - b + 1)*10^(k - 1) 을 따른다.
        a = L // 10
        b = U // 10
        # print((b-a+1) * k * 45)
        return_num += (b-a+1) * k * 45

        k *= 10
        L //= 10
        U //= 10
    
    # n이 마지막 자리 수 일 때
    else:
        for i in range(L,U+1):
            return_num += k * i
        print(return_num)
        exit()

print(return_num)