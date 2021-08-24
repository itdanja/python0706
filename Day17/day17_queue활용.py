#문제1
# 콜센터의 응답 대기 시간 계산해서 출력
    # 사용관련 6분
    # 고장관련 3분
    # 환불관련 4분

# 상담 순서  :    사용 , 고장 , 환불 , 환불 , 고장
#대기시간        0  , 6   ,  9  , 13  ,  17

def isqueuefull() : #  큐가 다 찾는 확인 함수
    global SIZE , queue , front , rear # 전역변수
    if rear != SIZE-1 : # 다 찬 경우가 아니면
        return False
    elif rear == SIZE-1 and front == -1 :
        return True # 다 찬 경우
    else:
        for i in range( front+1 , SIZE ):   # 남아있는 데이터를 한칸씩 이동
            queue[i-1] = queue[ i ]
            queue[i] = None
        front -= 1  # 데이터 삭제시
        rear -= 1   # 데이터 삭제시
        return  False
#2.
def isqueueempty() : # 큐가 다 비어있는지 확인 함수
    global SIZE , queue , front , rear
    if front == rear : #  front rear 같을경우
        return True
    else:
        return False
#3.
def enqueue(data) : # 큐에 데이터 추가
    global SIZE, queue, front, rear
    if isqueuefull() :
        print(" 큐가 다 찼습니다. ")
        return
    rear += 1   # rear 1 증가
    queue[rear] = data # rear 위치에 값넣기
#4.
def dequeue() : # 큐에 데이터 삭제
    global SIZE, queue, front, rear
    if isqueueempty() :
        print("큐가 비어있습니다")
        return None
    front += 1 # front 1 증가
    data = queue[front]
    queue[front] = None # front 위치에 데이터 삭제
    return data
#5.
def peek() : # front+1 위치의 데이터를 확인 하는 함수
    global SIZE, queue, front, rear
    if isqueueempty() :
        print("큐가 비어 있습니다 ")
        return None
    return queue[front+1]

#전연변수
SIZE = 6
queue =[ None for _ in range(SIZE) ]
front = 0 # 시작위치 의 초기값
rear = 0  #

waitCall = [ ('사용',6) , ("고장",3) , ("환불",4) , ("환불",4) , ("고장",3) ]

for call in waitCall :
    print(" 귀하의 대기 예상시간은 " , 시간함수만들기  , "분 입니다")
    print(" 현재 대기 콜 --> " , queue )
    enqueue( call )




