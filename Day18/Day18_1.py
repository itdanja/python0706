
# 자료구조 [ 데이터를 저장하는 방법 : 스택 , 큐 ]

# 이진트리 :  각각의 노드가 최대 두 개의 자식 노드를 가지는 트리 자료 구조로
    # 1. 컴퓨터 폴더
    # 2. 정렬과 검색
    # 3. 하나의 노드의 왼쪽자식노드 와 오른쪽자식노드

# 파이썬에서 완전이진트리의 생성 예
class TreeNode() :
    def __init__(self):
        self.left = None    # 왼쪽노드의 위치
        self.data = None    # 현재노드의 값
        self.right = None   # 오른쪽노드의 위치

node1 = TreeNode() # 해당클래스의 객체 생성
node1.data = "유재석"

node2 = TreeNode() # 해당클래스의 객체 생성
node2.data = "강호동"
node1.left = node2

node3 = TreeNode()
node3.data = "신동엽"
node1.right = node3

node4 = TreeNode()
node4.data = "서장훈"
node2.left = node4

node5 = TreeNode()
node5.data ="김희철"
node2.right = node5

node6 = TreeNode
node6.data ="우원재"
node3.left = node6

print( node1.data , end=" ")
print( )
print( node1.left.data ,"   " + node1.right.data )
print()
print( node1.left.left.data, " " , node1.left.right.data , " ", node1.right.left.data)






