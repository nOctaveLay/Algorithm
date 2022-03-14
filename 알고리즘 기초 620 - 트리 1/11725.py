'''
루트 없는 트리가 주어진다. 이 때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 알고리즘을 구하시오.

입력 : 
첫째 줄 :노드의 개수 N
두번째 줄 부터 N-1 줄에 트리 상에서 연결된 두 정점

출력 :
부모 노드 번호를 2번 노드부터 순서대로 출력

'''

'''
thinking
1. 이진 트리인가? => 그런 말은 문제에 존재하지 않음
2. 트리에서 부모는 한 명만 존재한다.
3. 부모가 이미 있다면, 나머지 관계들은 모두 자식 관계이다.
   => 즉, 나머지 관계에서 자기 자신이 부모 관계이다.
'''

import sys

'''
recursion 짜는 연습을 확실히 해 둘것.
'''

def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i] == -1:
            parents[i] = start
            dfs(i,tree,parents)

if __name__ == "__main__":
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    num_of_node = int(input())
    tree = [[] for _ in range(num_of_node+2)]
    parent_list = [-1 for _ in range(num_of_node+1)]

    for _ in range(num_of_node-1):
        node1_data, node2_data = map(int,input().rstrip("\n").split(" "))
        # 관계가 있음을 표현
        tree[node1_data].append(node2_data)
        tree[node2_data].append(node1_data)

    dfs(1,tree,parent_list)
    print(*parent_list[2:],sep='\n')
