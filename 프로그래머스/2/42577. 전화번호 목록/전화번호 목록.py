def solution(phone_book):
    # 자신을 제외한 다른 element와 비교해야한다.
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return한다.
    # phone_book 의 길이가 1이상 1000000 (O^6) 이하이므로, 최대한 nlgn 이상을 넘어가선 안된다
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        a = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:a]:
                return False
    return True
            
            