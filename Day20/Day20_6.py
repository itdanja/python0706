
import random
# 순차검색 , 이진검색 성능비교
def seqsearch( ary , fdata) :
    global count        # 비교 횟수
    pos = -1
    for i in range( len(ary) ) :
        count += 1
        if ary[i] == fdata :
            pos = i
            break
    return pos

def binsearch( ary , fdata ) :
    global count
    start = 0
    end = len(ary) -1

    while start <= end :
        count += 1
        mid = (start + end) // 2

        if fdata == ary[mid] :
            return mid
        elif fdata > ary[mid] :
            start = mid +1
        else:
            end = mid -1
    return  -1


dataary , sortedary = [],[]
finddata = 7878
count = 0

dataary = [ random.randint(0 , 999999) for _ in range(1000000) ]
dataary.insert( random.randint(0,1000000) , finddata )
sortedary = sorted( dataary )

print( "#비정렬 배열(100만개)-->" , dataary[0:5],"~~~" , dataary[-5:len(dataary)])
print( "비정렬 배열(100만개)-->" , sortedary[0:5],"~~~" , dataary[-5:len(sortedary)])

count = 0
pos = seqsearch( dataary , finddata )
if pos != -1 :
    print(" 순차 검색(비정렬 데이터) --> " , count ,"회")

count = 0
pos = binsearch( sortedary , finddata )
if pos != -1 :
    print(" 이진 검색(정렬 데이터) --> " , count ,"회")
























