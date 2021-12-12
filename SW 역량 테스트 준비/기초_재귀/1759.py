import sys
input = sys.stdin.readline

L,C = list(map(int,input().split()))
alph_list = sorted(input().rstrip("\n").split())
checked = [0 for i in range(C)]
vowel_list = ['a', 'e', 'i', 'o', 'u']
answer = []
def solve(start,k):
    
    global answer
    if k == 0:
        vowel_check = 0
        cons_check = 0
        for x in answer:
            if x in vowel_list: vowel_check += 1
            else: cons_check += 1
        if vowel_check > 0 and cons_check > 1 :
            answer_string = ''.join(answer)
            sys.stdout.write(f'{answer_string}\n')
        return
    else:
        for i in range(start,len(alph_list)):
            if checked[i] == 0:
                answer.append(alph_list[i])
                checked[i] = 1
                solve(i+1,k-1)
                checked[i] = 0
                answer.remove(alph_list[i])
            
solve(0,L)