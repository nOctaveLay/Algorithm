def solution(s):
    answer = True
    s_stack = []
    for s_c in s:
        if s_c == '(':
            s_stack.append('(')
        else:
            if len(s_stack) > 0:
                s_stack.pop()
            else:
                return False
    if len(s_stack) > 0 : return False
    else : return True