import sys
input = sys.stdin.readline
s, n = input().rstrip("\n").split()
s = int(s)

def rl(s):
    return f'{" "*(s+1)}|'
def ll(s):
    return f'|{" "*(s+1)}'
def dl(s):
    return f'|{" "*(s)}|'
def wl(s):
    return f' {"-"*s} '
def nl(s):
    return f' {" "*s} '

answer_string = ['' for _ in range(2*s + 3)]
mid = (2*s + 3)//2
last = 2*s + 3

for i in n:
    # 위의 --가 있는 경우
    if int(i) in [2,3,5,6,7,8,9,0]:
        answer_string[0] += wl(s)
        # 위의 --가 있는 경우 중 중간 / 아래에 -- 가 없는 경우는 7 0뿐이다.
        if not i == '7':
            answer_string[-1] += wl(s)
            if not i == '0': answer_string[mid] += wl(s)
            else: answer_string[mid] += nl(s) 
        else: 
            answer_string[-1] += nl(s)
            answer_string[mid] += nl(s)
    else:
        answer_string[0] += nl(s)
        answer_string[-1] += nl(s)
        if i == '4': answer_string[mid] += wl(s)
        else:answer_string[mid] += nl(s)
    
        
    # 오른쪽 |만 있는 경우
    if int(i) in [1,2,3,7]:
        for j in range(1,mid):
            answer_string[j] += rl(s)
        for j in range(mid+1,last - 1):
            answer_string[j] += rl(s) if i != '2' else ll(s)
    else:
    # 왼쪽 l만 있는 경우
        if int(i) in [5,6]:
            for j in range(1,mid):
                answer_string[j] += ll(s)
            for j in range(mid+1, last - 1):
                answer_string[j] += rl(s) if i == '5' else dl(s)
    # 둘 다 있는 경우
        else:
            for j in range(1,mid):
                answer_string[j] += dl(s)
            for j in range(mid+1, last-1):
                answer_string[j] += dl(s) if i == '8' or i == '0' else rl(s)

    # 문자 끝나고 하나 띄어줘야 하기 때문            
    for i in range(len(answer_string)):
        answer_string[i] += ' '

for k in answer_string:
    print(*k,sep='')