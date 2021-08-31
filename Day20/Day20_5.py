from operator import itemgetter

# 도서검색 이진검색으로 구현

def makeindex( ary , pos ) :
    beforeary = []
    index = 0
    for data in ary :
        beforeary.append( (data[pos] , index ) )    # beforeary 에 데이터 , 인덱스번호
        index +=1

    sortedary = sorted( beforeary , key=itemgetter(0))
    return sortedary

def bookSearch( ary , fdata ) :
    pos = -1
    start = 0
    end = len(ary) -1

    while start <= end :
        mid = (start+end) // 2
        if fdata == ary[mid][0] :   # 데이터가 동일한 경우
            return  ary[mid][1]     # 찾은 데이터의 인덱스
        elif fdata > ary[mid][0] :
            start = mid + 1
        else:
            end = mid -1
    return pos

bookary = [ ["어린왕자","쌩떽쥐베리"],["이방인","까뮈"],["부활","톨스토이"] ,
            ["신곡","단테"],["돈키호테","세르반테스"],["동물농장","조지오웰"],
            ["데미안","헤르만헤세"],["파우스트","괴테"] ,["대지","펄벅"] ]

nameindex = [ ] # 책이름의 인덱스 순서
nameindex = makeindex( bookary , 0)
print(" 도서명 인덱스 표 --> " , nameindex )

authindex = [ ] # 작가의 인덱스 순서
authindex = makeindex( bookary , 1 )
print(" 작가명 인덱스 표 --> " , authindex )

# 문제 1: 도서명 입력받아 작가명 반환
findname = input(" 검색 도서명 : ")
findpos = bookSearch( nameindex , findname )
if findpos != -1 :
    print(findname , "의 작가는 ",bookary[findpos][1],"입니다")
else:
    print(findname , "책은 없습니다 ")

# 문제 2: 작가명 입력받아 도서명 반환
findname = input(" 검색 작가명 : ")
findpos = bookSearch( authindex , findname )
if findpos != -1 :
    print( findname , "의 도서는 " , bookary[findpos][0],"입니다")
else:
    print(findname , "작가는 없습니다 ")














