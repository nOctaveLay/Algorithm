str_n = input()
n = int(str_n)
digit_num = list()
return_list = [0 for i in range(10)]
num_count = 1

while True:

    # 끝 자리가 9가 아니라면 9로 만들어주는 과정을 거쳐야한다.
    # 만약 1-9일 경우, 0의 자리는 빼줘야 한다.
    
    while n % 10 != 9 and n != 0:
        # 예를 들어 39라는 수가 있으면 return_list[3] += 1, return_list[9] += 1
        for i in str(n):
            return_list[int(i)] += num_count
        n -= 1

    # n이 2자리 수가 넘을 경우
    if n > 9:
        # n이 k자리수라고 가정했을 때, (단 k >= 2)
        # k-1 자리수[즉, 1.. ~ n/10] 의 0-9까지의 갯수는 (10/10 - b + 1)*10^(k - 1) 을 따른다.
        b = n // 10
        for i in range(10):
            return_list[i] += (b+1) * num_count

        
    # n이 마지막 자리 수 일 때
    else:
        for i in range(1,n+1):
            return_list[i] += num_count
        break

    return_list[0] -= num_count
    num_count *= 10
    n //= 10 

for s in return_list:
    print(s, end = ' ')