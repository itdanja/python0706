

# 검색
    # 순차 검색 , 이진 검색 , 트리 검색 등
    # 검색한 값의 인덱스 위치 검색

# 정렬이 없는 상태의 순차검색
def seqSearch( ary , fdata) :
    pos = -1 # 검색된 인덱스 위치 [ -1는 검색결과가 없다 ]
    size = len(ary)

    print("## 비교할 데이터 --> " , end=" ")
    for i in range(size) :
        print( ary[i] , end=" ")
        if ary[i] == fdata :
            pos = i
            break
    print()
    return pos

dataary = [ 188 , 150 , 168 , 162 , 105 , 120 , 177 ,50]
fimdata = int( input("찾을값을 입력하세요 --> "))
position = seqSearch( dataary , fimdata)
if position == -1 :
    print(fimddata ," 결과 없음" )
else:
    print(fimdata , " 결과 : " , position, "위치에 존재 ")