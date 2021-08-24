
# 큐 : 먼저 집어 넣은 데이터가 먼저 나오는 구조
    # 1. 입구 , 출구
    # 2. 줄세우기 , 지하철 , 인쇄 등
    # 3. FIFO 선입선출

# 파이썬으로 큐 구현1
queue = [ None, None , None ,None , None ] # 5개 공백 요소 리스트
front = -1 # 나가는 인덱스 위치
rear =-1 # 들어오는 인덱스 위치

rear += 1   # 들어오는 인덱스 위치 증가
queue[rear] = "유재석"
rear += 1  # 들어오는 인덱스 위치 증가
queue[rear] = "신동엽"
rear += 1  # 들어오는 인덱스 위치 증가
queue[rear] = "서장훈"

print(" --------------------- 큐 상태 --------------------")
print('[출구] <---- ' , end=" ")
for i in range( 0 , len(queue)  ) :
    print(queue[i] , end =" ")
print("<---- [입구] ")

print(" ----------------------  : 데이터 추출 ------------- ")
front += 1 # 나가는 인덱스 위치
data = queue[front]
queue[front] = None
print( "dequeue ---> " , data )

front += 1 # 나가는 인덱스 위치
data = queue[front]
queue[front] = None
print( "dequeue ---> " , data )

front += 1 # 나가는 인덱스 위치
data = queue[front]
queue[front] = None
print( "dequeue ---> " , data )

print(" --------------------- 큐 상태 --------------------")
print('[출구] <---- ' , end=" ")
for i in range( 0 , len(queue)  ) :
    print(queue[i] , end =" ")
print("<---- [입구] ")


