import math
n,m = map(int,input().split(" "))

#표를 저장할 공간
Table_a = list()
for _ in range(n):
    Table_a.append(input())
seq_max_length = max(n,m) # 수열의 최대 길이
for seq_length in range(seq_max_length,0,-1): # 최대를 찾을 때에는 거꾸로 찾는 것이 빠르므로, 이렇게 쓰기로 하자.
    max_n_d = (n-1)//(seq_length-1) if seq_length > 1 else 0
    max_m_d = (m-1)//(seq_length-1) if seq_length > 1 else 0
    max_list = list()
    # 처음 위치
    for first_x in range(n):
        for first_y in range(m):

            # 움직이는 위치
            # 그런데 음수로 움직일 때도 있을거 같은데?
            # 단순히 빼주면 되지. <--- 한 번에 될까? 
            # 안됌 왜냐면 ++로 움직이고, --로만 움직이는게 아님, +-로도 움직이고 -+로도 움직임
            # 원리는 같음. 그러면 어떻게 해주면 좋을까?

            for n_d in range(max_n_d+1):
                for m_d in range(max_m_d+1):
                    seq_list = [0 for _ in range(4)]
                    if seq_length > 1 and n_d == 0 and m_d == 0: continue

                    if first_x + n_d * seq_length < n :
                        if first_y + m_d * seq_length < m:
                            seq_list[0] = ''
                        if first_y - m_d * seq_length >= 0 :
                            seq_list[1] = ''
                    if first_x - n_d * seq_length >= 0:
                        if first_y + m_d * seq_length < m:
                            seq_list[2] = ''
                        if first_y - m_d * seq_length >= 0:
                            seq_list[3] = ''
                
                    for l in range(0,seq_length):
                        x_1 = first_x + n_d * l
                        x_2 = first_x - n_d * l
                        y_1 = first_y + m_d * l
                        y_2 = first_y - m_d * l

                        if seq_list[0] == '':
                            seq_list[0] += Table_a[x_1][y_1]
                        if seq_list[1] == '':
                            seq_list[1] += Table_a[x_1][y_2]
                        if seq_list[2] == '':
                            seq_list[2] += Table_a[x_2][y_1]
                        if seq_list[2] == '':
                            seq_list[2] += Table_a[x_2][y_2]
                    
                    print(seq_list)

                    for seq in seq_list:
                        if seq != '':
                            num = int(seq)
                            num_root = math.isqrt(num)
                            if num_root * num_root ==  num:
                                max_list.append(num)


if len(max_list) != 0 and max(max_list) != 0:
    print(max(max_list))
    
if len(max_list) == 0:
    print(-1)