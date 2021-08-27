
# 선택 정렬 , 퀵정렬  , 버블 정렬 등등

# 버블정렬
def BubbleSort( ary ) :
    n = len(ary)    # 리스트의 길이
    count = 0 # 비교 횟수 체크 변수
    for end in range( n-1 , 0 , -1  ) : # 마지막 인덱스부터 시작해서 처음인덱스까지
        changeYN = False # 자리 바꿈이 발생했는지 확인 하는 변수
        for cur in range( 0 , end ) :   # 첫번째 인덱스부터 마지막 인덱스
            count += 1
            if ary[cur] > ary[cur+1] : # 오름차순 >     # 내림차순 <
                ary[cur] , ary[cur+1] = ary[cur+1] , ary[cur]
                changeYN = True
        if not changeYN :
            break
    return ary , count

# 버블 정렬
dataAry = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
            #
# 정렬 전
print( " 정렬 전 " , dataAry )
# 정렬 후
dataAry = BubbleSort(dataAry)
print( " 정렬 후 " , dataAry )
