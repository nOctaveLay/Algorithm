#파이프를 이용한 방식으로 구현 필요
from asyncio.subprocess import PIPE
from itertools import product
import sys, subprocess
import os
input = sys.stdin.readline

problem_num = 6064

current_folder_route = os.path.dirname(os.path.realpath(__file__))
file_name1 = f'{current_folder_route}/{problem_num}.py'
file_name2 = f'{current_folder_route}/{problem_num}_another.py'
fIO = f'{current_folder_route}/input.txt'
fERR = f'{current_folder_route}/err.txt'
try_num = 0
for m,n in product(range(1,40000),repeat=2):
    for x in range(1,m):
        for y in range(1,n):
            print(try_num,")","m:",m,"n:",n,"x:",x,"y:",y,end=' ')
            with open(fIO,'w') as finput:
                finput.write(f'{m} {n} {x} {y}')
            with open(fIO,'r') as finput:    
                proc1 = subprocess.run(['python',file_name1],stdin = finput, stdout = PIPE)
            with open(fIO,'r') as finput:    
                proc2 = subprocess.run(['python',file_name2],stdin = finput, stdout = PIPE)
            if proc1.stdout != proc2.stdout:
                print('different')
                with open(fERR,'w') as ferror:
                    ferror.write(f'{m} {n} {x} {y} : {proc1.stdout} | {proc2.stdout}')
            else:
                print("Success")
            try_num += 1
print("finish")