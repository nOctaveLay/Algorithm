'''
1. 이진 트리를 입력받는다고 했으므로, 이진 트리를 만들어야 한다.
2. 트리에서 가장 큰 핵심은 노드를 구현하는 것이며, 이는 다음과 같은 구성요소를 갖고 있다.
    1. 저장할 자료
    2. 부모 노드를 가리키는 포인터
    3. 자손 노드를 가리키는 포인터이다.

+ 노드에서 바로 tree 구현체를 짜려고 하니 매우 어려웠다.
+ 그래서 tree 구현체를 dict로 따로 짰다.
+ dict는 key만 알고 있다면 find하는 시간이 O(1)이므로, 효율적이라고 생각한다.

'''
class Node:
    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        self.data = data

def preorder(node): 
    print(node.data,end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data,end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.data,end='')

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    tree = dict()
    for _ in range(N):
        node, left, right = input().rstrip("\n").split()
        tree[node] = Node(node,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])