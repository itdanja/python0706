import random
import time
# 선택 정렬과 퀵 정렬의 차이

# 선택 정렬
def selectionSort( ary ) :
    n = len(ary) # 리스트 길이
    for i in range( 0 , n-1) :  # 인덱스는 0 부터 마지막 번호 전까지
        minIdx = i                      # i 는 현재 인덱스 위치
        for k in range( i+1 , n ) :     # 현재 인덱스 의 다음인덱스부터 끝 인덱스 까지
            if ary[minIdx] > ary[k] :
                minIdx = k
            tmp = ary[i]                # 스왑
            ary[i] = ary[minIdx]
            ary[minIdx] = tmp
    return ary

# 퀵 정렬
def qsort( ary , start , end ) :
    if end <= start :
        return
    low = start     # 첫번째 인덱스
    high = end      # 마지막 인덱스

    pivot = ary[ (low+high)//2 ] # 작은값은 왼쪽  , 큰값은 오른쪽 분리
    while low <= high :
        while ary[low] < pivot : # 왼쪽보다 중간값이 더 크면
            low += 1               # 왼쪽에 +1
        while ary[high] > pivot :   # 오른쪽이 중간값보다 더 크면
            high -= 1               # 오른쪽 -1
        if low <= high : # 오른쪽 더 크면
            ary[low] , ary[high] = ary[high] , ary[low]
            low , high = low+1 , high - 1
    mid = low

    qsort( ary , start , mid - 1 ) # 재귀
    qsort( ary , mid , end)         # 재귀

def quicjsort( ary) :
    qsort( ary , 0 , len(ary)-1 )

countary = [ 1000 , 10000 , 12000 , 15000 ]

for count in countary :
    tempary = [ random.randint(10000,99999) for _ in range(count)]
    selectary = tempary[:]
    quickary = tempary[:]

    print(" 데이터 수 : ", count , "개")
    start = time.time()
    selectionSort(selectary)
    end = time.time()
    print("선택 정렬 --> %10.3f 초" % (end-start) )

    start = time.time()
    quicjsort(quickary)
    end = time.time()
    print("퀵 정렬 --> %10.3f 초" % (end - start))

    count *=5









































