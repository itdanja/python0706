
# 도서관 책 목록의 관리/검색을 이진트리로 구현하기
import random
#노드 클래스
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역변수
memory = [ ]
rootBook , rootAuth = None , None
bookAry = [ ["어린왕자" , "생떽쥐베리"] , ["이방인", "까뮈"] , [ "부활" , "풀스토리" ] ,
            ["신곡" , "단테"],["돈키호테","세르반테스"],["동물농장","조이오웰"] ,
            ["데미안","헤르만헤세"] , ["파우스트","괴테"] , ["대지" , "펄벅"] ]

random.shuffle( bookAry )

# 책 이름으로 트리 구성 하기
node = TreeNode( )
node.data = bookAry[0][0] # 첫번째 도서를 root노드에 값 값넣기
rootBook = node
memory.append( node )

# 반복문을 통해서 각 노드에 담기
for book in bookAry[ 1 : ] :
    name = book[0]
    node = TreeNode()
    node.data = name

    current = rootBook

    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else:
            if current.right == None :
                current.right = node
                break
            current = current.right
    memory.append(node)

print( " 책 이름 트리 구성 완료 ")

#저자 기준으로 트리 구성
node = TreeNode()
node.data = bookAry[0][1]
rootAuth = node
memory.append( node )

for book in bookAry[ 1 : ] :
    name = book[1]
    node = TreeNode()
    node.data = name

    current = rootAuth
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

if bookOrAuth == 1 :
    root = rootBook
else:
    root = rootAuth

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
        current = current.left
    else :
        if current.right ==None :
            print(findname , "을 목록에 없음")
            break
        current = current.right
















