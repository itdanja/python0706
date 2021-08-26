# 문제1
# 	*편의점에서 판매된 물건 목록 출력하는 이진트리 구조 구현
# 	1. 여러개 제품을 판매했을경우 중복을 제외한 오늘 판매한 제품만 출력

import random

class TreeNode( ) :
	def __init__(self):
		self.left = None  # 왼쪽 자식 노드
		self.data = None # 현 노드 데이터
		self.right = None # 오른쪽 자식노드

# 편의점 파는 물건 목록
dataAry = [ "바나나맛우유" , "레스비캔커피" , "츄파춥스" ,"도시락" , "삼다수","코카콜라","삼각김밥"]

# 랜덤으로 판매한 물건 목록
sellAry = [ random.choice(dataAry) for _ in range(20) ]
				# random.choice( 리스트 ) : 리스트내 요소중 하나를 랜덤 선택

print("오늘 판매된 물건 (중복o) --> " , sellAry )

#중복제거를 한 이진 탐색트리
memory = [ ] # 여러 노드 리스트
root = None # root 노드

node = TreeNode()
node.data = sellAry[0] #첫번째 제품을 root
root = node
memory.append(node)

for name in sellAry[ 1 : ] : # 첫번째 제품을 제외한 두번째 제품부터
	node = TreeNode()
	node.data = name

	current = root # current 현재 노드의 위치
	while True :
		if name == current.data : # 현재노드와 name 동일하면 중복제거
			break # 중복제거
		if name < current.data :
			if current.left ==None : # 만약에 왼쪽노드가 공백이면 왼쪽노드에 데이터 넣기
				current.left = node
				memory.append(node)
				break
			current = current.left # 만약에 공백이 아니면 왼쪽 노드로 이동
		else:
			if current.right == None :
				current.right = node
				memory.append( node )
				break
			current = current.right

def preorder( node ):
	if node == None :
		return
	print( node.data , end=" ")

	preorder( node.left ) # 재귀
	preorder( node.right )

print("오늘 판매된 물건 (중복x) --> " , end = " " )
preorder(root)






















