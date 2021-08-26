
# 도서관 책 목록의 관리/검색을 이진트리로 구현하기
import random # 도서 순서를 랜덤으로 바꾸기한 랜덤 함수
#노드 클래스
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역변수
memory = [ ] # 노드 저장순서
rootBook , rootAuth = None , None
bookAry = [ ["어린왕자" , "생떽쥐베리"] , ["이방인", "까뮈"] , [ "부활" , "풀스토리" ] ,
            ["신곡" , "단테"],["돈키호테","세르반테스"],["동물농장","조이오웰"] ,
            ["데미안","헤르만헤세"] , ["파우스트","괴테"] , ["대지" , "펄벅"] ]

random.shuffle( bookAry ) # 도서를 랜덤으로 배치

# 책 이름으로 트리 구성 하기
node = TreeNode( )
node.data = bookAry[0][0] # 첫번째 도서의 도서명
rootBook = node # 최상위 노드 에 첫번째 도서의 도서명 넣기
memory.append( node ) #

# 반복문을 통해서 각 노드에 담기
for book in bookAry[ 1 : ] : # 첫번째 도서를 제외한 두번째 도서부터
    name = book[0]  # 도서명
    node = TreeNode()
    node.data = name

    current = rootBook # 현재위치는 최상의노드

    while True :
        if name < current.data : # current 노드보다 작으면
            if current.left == None : # 왼쪽이 공백이면
                current.left = node  # 왼쪽자식노드에 노드 넣기
                break
            current = current.left # 공백이 아니면 또 왼쪽으로 이동
       else:       # current 노드보다 크면
            if current.right == None :  # 오른쪽이 공백이면
                current.right = node    # 오른쪽자식노드에 노드 넣기
                break
            current = current.right # 공백이 아니면 또 오른쪽 이동
    memory.append(node) # 자식노드를 리스트에 추가

print( " 책 이름 트리 구성 완료 ")

#저자 기준으로 트리 구성
node = TreeNode()
node.data = bookAry[0][1] # 첫번째 도서의 저자
rootAuth = node # 최상위 노드 에 첫번째 도서의 저자 넣기
memory.append( node )

for book in bookAry[ 1 : ] :  # 첫번째 도서를 제외한 두번째 도서부터
    name = book[1] # 저자
    node = TreeNode()
    node.data = name

    current = rootAuth # 현재위치는 최상의노드

    while True :
        if name < current.data :
            if current.left ==None :
                current.left = node
                break
            current = current.left
        else:
            if current.right ==None :
                current.right = node
                break
            current = current.right
    memory.append(node)

print("작가 이름 트리 구성 완료 ")

bookOrAuth = int(input("책검색(1) , 작가검색(2) --> "))
findname = input(" 검색할 책 이름 또는 작가 : --> ")

if bookOrAuth == 1 : # 1번 선택시
    root = rootBook     #도서명 노드
else:               # 그외 선택시
    root = rootAuth       # 저자명 노드

current = root

while True :
    if findname == current.data :
        print( findname , "을 찾음.")
        findYN = True
        break
    elif findname < current.data :
        if current.left == None :
            print(findname, "가 목록에 없음 ")
            break
        current = current.left  # 찾는값이 현재 노드의 값보다 작으면 왼쪽으로 이동
    else :
        if current.right ==None :
            print(findname , "을 목록에 없음")
            break
        current = current.right # 찾는값이 현재 노드의 값보다 크면 오른쪽으로 이동
















