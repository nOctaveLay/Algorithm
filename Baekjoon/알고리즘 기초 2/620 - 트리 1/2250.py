'''
# 2250.

이진트리를 그릴 때 각 레벨의 너비는 그 레벨에 할당된 노드 중 가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다.

임의의 이진 트리가 입력으로 주어질 때 
너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 프로그램을 구하여라

입력 : 
첫째 줄 : 노드의 개수 정수 N (1<=N<=10000)
다음 줄 : 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호

노드의 번호는 1~N까지, 자식이 없는 경우에는 자식의 노드 번호에 -1이 주어짐. 

출력 :
너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력.


'''


'''
이 문제에서 제일 까다로웠던 것은
1. root 노드가 1이라는 말이 어디에도 없다는 점 -> 따라서 root 노드의 data를 찾아줘야 했다는 점.
2. 그럼 이 root 노드를 어떻게 할까? dict을 이용해 tree노드를 짠다는 시점에서 이미 parent를 이용한 전략은 물건너갔다고 생각함.
3. 따라서 노드를 전부 세줌, 그리고 그 node부터 inorder를 진행.

'''

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

num = 1
def inorder(node,level):
    global num
    if node.left != -1:
        inorder(tree[node.left],level+1)
    distance[level].append(num)
    num += 1 
    if node.right != -1:
        inorder(tree[node.right],level+1)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    tree = dict()
    distance = [[] for _ in range(n+1)] 
    node_count = [-1 for i in range(n+1)]
    root = 1 

    for _ in range(n):
        data,left,right = list(map(int,input().rstrip("\n").split()))
        node_count[data] += 1
        if left != -1:
            node_count[left] += 1
        if right != -1:
            node_count[right] += 1
        tree[data] = Node(data,left,right)

    for i in range(1,n+1):
        if node_count[i] == 0:
            root = i

    inorder(tree[root],1)
   
    result = max(distance[1])-min(distance[1])+1
    large_num = 1

    for i in range(2,len(distance)):
        if distance[i]:
            minus_num = max(distance[i])-min(distance[i])+1
            if result < minus_num:
                result = minus_num
                large_num = i
    print(large_num,result,end='')