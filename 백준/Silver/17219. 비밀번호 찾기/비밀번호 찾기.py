n,m=map(int,input().split())
id_to_pw = dict()
for _ in range(n):
    s_id, s_pw = input().rstrip().split()
    id_to_pw[s_id] = s_pw
for _ in range(m):
    print(id_to_pw[input().rstrip()])