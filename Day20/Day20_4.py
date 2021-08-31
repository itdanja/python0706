
# 이진 검색 구현
def binSearch( ary , fdata ) :
    pos = -1 # 찾은 데이터의 인덱스 위치 [ -1 : 찾은 인덱스가 없을경우 ]
    start = 0   # 첫번째 인덱스
    end = len(ary) -1   # 마지막 인덱스

    while start <= end : # end가 같거나 클경우에만 실행
        mid = (start + end) // 2 # 중간값 구하기
        if fdata == ary[mid] : # 중간값과 찾는값이 같으면
            return mid          # 검색완료
        elif fdata > ary[mid] : # 중간값보다 더 크면 오른쪽으로 이동
            start = mid + 1     #  [ start는 mid의 앞으로 이동 ]
        else:                   # 중간값보다 더 작으면 왼쪽으로 이동
            end = mid - 1       # [ end는 mid의 뒤로 이동 ]\

    return pos

dataary = [50,60,105,120,150,160,162,168,177,188] # 정렬이 되어 있는 가정하에 리스트
finddata = int( input(" 검색 : ") )
result =  binSearch( dataary , finddata )
if result == -1 :
    print( finddata , "가 없습니다 ")
else:
    print( finddata , "는 ", result,"위치에 있습니다 ")
