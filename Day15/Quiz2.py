
#문제7 : 두 리스트를 합쳐서 오름차순 정렬

# 방법1
def solution ( arrA , arrB ) :
    arrA_idx = 0  # A리스트의 비교대상 현재 위치 변수
    arrB_idx = 0  # A리스트의 비교대상 현재 위치 변수
    result = [ ] # a b 합친 리스트

    while arrA_idx < len( arrA ) and arrB_idx <len( arrB ) :
        #  두리스트의 현재 비교대상위치가 마지막이 아니면
        if arrA[ arrA_idx ] < arrB[arrB_idx ] : # 만약에 A가 더 작으면
            result.append( arrA[arrA_idx ] )    # 결과리스트에 A 저장
            arrA_idx += 1                       # A리스트의 비교대상 현재위치 증가
        else :                                  # B가 더 작으면
            result.append( arrB[arrB_idx] )     # 결과리스트에 B 저장
            arrB_idx += 1                       # B리시트의 비교대상 현재위치 증가

    # 만약에 A리스트만 비교대상이 남았을경우 남은 요소를 결과에 넣기
    while arrA_idx < len( arrA ) :
        result.append( arrA[arrA_idx] )
        arrA_idx += 1
   # 만약에 B리스트만 비교대상이 남았을경우 남은 요소를 결과에 넣기
    while arrB_idx < len( arrB ) :
        result.append( arrB[arrB_idx] )
        arrB_idx += 1
    return result

arrA = [ -2 , 3 , 5 , 9 ]
arrB = [ 0 , 1 , 5 ]
result = solution( arrA , arrB )
print( " 문제7 결과 : " , result )

# 방법2
list = arrA+arrB
list.sort()
print( " 문제7 결과2" ,  list )


