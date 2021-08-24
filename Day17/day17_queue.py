
# 함수
    # 1. isqueuefull()  큐가 다 찼는지 확인 함수
    # 2. isqueueempty() 큐가 다 비어있는지 확인 함수
    # 3. enqueue()      큐에 데이터 삽입 함수
    # 4. dequeue()      큐에 데이터 삭제 함수
    # 5. peek()         front 위치에 데이터 확인 함수

#1.
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
SIZE = int( input(" 큐의 크기를 입력 : "))
queue =[ None for _ in range(SIZE) ]
front = -1 # 시작위치 의 초기값
rear = -1  #

#메뉴
select = input("삽입[I] / 추출[E] / 확인[V] / 종료[X] 중 하나 선택 : ")

while select !="x" and select !="X" :
    if select =="I" or select == "i" :
        data = input(" 입력할 데이터 : ")
        enqueue(data)
        print( " 큐 상태 : ",queue )
    elif select == "E" or select == "e":
        data = dequeue()
        print(" 추출된 데이터 : ", data)
        print(" 큐 상태 : ", queue)
    elif select == "V" or select == "v":
        data = peek()
        print(" 확인된 데이터 : ", data)
        print(" 큐 상태 : ", queue)
    else:
        print("알수없는 행동입니다")
    select = input("삽입[I] / 추출[E] / 확인[V] / 종료[X] 중 하나 선택 : ")

print(" 큐 프로그램 종료 ")































