
#퀵정렬 : 기준과 비교 하여 왼쪽 / 오른쪽 그룹
def quickSort(ary) :
    n = len(ary) # 리스트 길이
    if n <= 1 : # 1 이하이면 정렬 종료
        return ary

    pivot = ary [ n // 2 ]     # 기준 값을 중간값으로 지정
    print()
    print( "기준" , pivot , end = " " )
    leftAry , rightAry = [ ] , [ ]

    for num in ary :
        if num < pivot : # 기준 보다 작으면 왼쪽
            leftAry.append( num )
        elif num > pivot :
            rightAry.append( num )

    print("왼쪽 그룹 : " , leftAry , " 오른쪽 그룹 :  " , rightAry )

    return quickSort(leftAry) + [ pivot ] + quickSort(rightAry)      # 재귀함수

dataAry = [ 188 , 150 , 168 , 162 , 105 , 120 , 177 , 50 ]

print(" 정렬 전 --> " , dataAry )
dataAry = quickSort( dataAry )
print(" 정렬 후 --> " , dataAry )

