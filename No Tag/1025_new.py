import math
n,m = map(int,input().split(" "))

#표를 저장할 공간
Table_a = list()
for _ in range(n):
    Table_a.append(input())
seq_max_length = max(n,m) # 수열의 최대 길이
max_list = list()
for seq_length in range(seq_max_length,0,-1): # 최대를 찾을 때에는 거꾸로 찾는 것이 빠르므로, 이렇게 쓰기로 하자.
    max_n_d = (n-1)//(seq_length-1) if seq_length > 1 else 0
    max_m_d = (m-1)//(seq_length-1) if seq_length > 1 else 0


    # 처음 위치
    for first_x in range(n):
        for first_y in range(m):

            # 움직이는 위치
            # 그런데 음수로 움직일 때도 있을거 같은데?
            # 단순히 빼주면 되지. <--- 한 번에 될까?

            for n_d in range(max_n_d+1):
                for m_d in range(max_m_d+1):
                    seq_list = ['' for _ in range(4)]

                    for l in range(0,seq_length):

                        if seq_length > 1 and n_d == 0 and m_d == 0:
                            seq_list = ['' for _ in range(4)]
                            continue

                        if first_x+n_d*l < n and first_y+m_d*l < m:
                            seq_list[0] += Table_a[first_x+n_d*l][first_y+m_d*l]

                        if (first_x-n_d*l) >= 0 and (first_y-m_d*l) >= 0:
                            seq_list[1] += Table_a[first_x-n_d*l][first_y-m_d*l]
                        
                        if (first_x+n_d*l) < n and first_y-m_d*l >= 0:
                            seq_list[2] += Table_a[first_x+n_d*l][first_y-m_d*l]
                        
                        if (first_x-n_d*l) >= 0 and first_y + m_d*l < m:
                            seq_list[3] += Table_a[first_x-n_d*l][first_y + m_d*l]
                    

                    for seq in seq_list:
                        if seq == '' or (len(seq) > 1 and seq[0] == '0'): continue
                        seq_num = int(seq)
                        if math.isqrt(seq_num)**2 == seq_num: max_list.append(seq_num)

if len(max_list) != 0:
    print(max(max_list))

if len(max_list) == 0:
    print(-1)